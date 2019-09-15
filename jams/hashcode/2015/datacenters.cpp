#include <cstdio>
#include <strings.h>
#include <utility>
#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <set>

using namespace std;

struct dc_position {
	int row;
	int gap;
};

struct server_t {
	int size;
	int capacity;
	int pool;
	dc_position pos;
};

dc_position search_gap(vector<vector<int>> dc, server_t s) {
	for (int i=0; i < dc.size(); i++) {
		for (int j=0; j < dc[i].size(); j++) {
			if (dc[i][j] >= s.size) {
				dc_position pos = {i, j};
				return pos;
			}
		}
	}

	dc_position pos = {-1, -1};

	return pos;
}

void print_dc(auto dc) {
	for (auto &row : dc) {
		for (int &gap : row) {
			cout <<gap <<" ";
		}
		cout <<endl;
	}
}

int main() {
	int R, S, U, P, M;
	scanf("%d %d %d %d %d\n", &R, &S, &U, &P, &M);

	int datacenter[R][S];
	bzero(datacenter, R *S * sizeof(int));

	pair<int, int> busy_slots[U];
	int a, b;
	for(auto &s : busy_slots) {
		scanf("%d %d\n", &a, &b);
		s = make_pair(a, b);
		datacenter[a][b] = -1;
	}

	for (auto &row : datacenter) {
		for (auto &slot : row) {
			cout <<((slot == -1) ? 'X': '_');
		}
		cout <<endl;
	}

	server_t servers[M];
	for (server_t &s : servers) {
		scanf("%d %d\n", &s.size, &s.capacity);
		s.pos.row = s.pos.gap = s.pool = 0;
	}

	cout <<R <<" " <<S <<" " <<P <<endl;

	/* The most important effect of the busy slots is that they split the
	 * row in several gaps of different sizes, and the server placement is
	 * subject to the size of those gaps. Lets define the datacenter as the
	 * list of those gaps (split by row)
	 */
	vector<vector<int>> dc;
	for (auto &row : datacenter) {
		vector<int> r;
		int gap_size = 0;

		for (auto &slot : row) {
			if ((slot == -1) && (gap_size > 0)) {
				r.push_back(gap_size);
				gap_size = 0;
			} else {
				gap_size++;
			}
		}

		if (gap_size > 0) {
			r.push_back(gap_size);
			gap_size = 0;
		}
	
		dc.push_back(r);
	}


	//vector<vector<int>> dc_status = dc;
	//vector<vector<set<*server_t>>> dc_servers;

	print_dc(dc);

	// Initial assignation of the servers and pools
	int p = 0;
	int pool_power[P] = {};
	int pool_row_power[R][P] = {};

	for(server_t &s : servers) {
		s.pos = search_gap(dc, s);
		if (s.pos.row >= 0) {
			dc[s.pos.row][s.pos.gap] -= s.size;
			pool_power[p] += s.capacity;
			pool_row_power[s.pos.row][p] += s.capacity;
			s.pool = p++;
		}

		//cout <<s.pos.row <<", " <<s.pos.gap <<endl;
	}

	cout <<"---\n";
	print_dc(dc);

	for (int & p : pool_power) {
		cout <<p <<" ";
	}
	cout <<endl;

}
