#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include "boost/multi_array.hpp"

using namespace std;

/*
vector<int> read_ints() {
	int i;
	string input;
	vector<int> vi;

	getline(cin, input);
	stringstream stream(input);

	while (myStream >> i) {
		vi.push_back(i);
	} 
	
	return vi;
}
*/

int min (int a, int b) {
	if (a < b) {
		return a;
	} else {
		return b;
	}
}

int find_silk(auto map, int H, int W, int i, int j) {
	int m, up, down, left, right;
	while (1) {
		up=down=left=right=90000;

		if (i > 0) up = map[i-1][j];
		if (j > 0) left = map[i][j-1];
		if (i < H - 1) down = map[i+1][j];
		if (j < W - 1) right = map[i][j+1];

		int a = min(up, down);
		int b = min(left, right);
		m = min(a, b);


		if (m >= map[i][j])
			return i*W + j;

		if (up == m) i -= 1;
		else if (left == m) j -= 1;
		else if (right == m) j += 1;
		else i+= 1;
	}
}

void solve() {
	int H, W;
	scanf("%d %d\n", &H, &W);

	typedef boost::multi_array<int, 2> array_type;
	array_type map(boost::extents[H][W]);

	for(int i=0; i<H; i++) {
		for(int j=0; j<W; j++) {
			scanf("%d", &map[i][j]);
		}
		scanf("\n");
	}

	for(int i=0; i<H; i++) {
		for(int j=0; j<W; j++) {
//			printf("%d ", map[i][j]);
		}
//		printf("\n");
	}

//	printf("\n");
	int silk[H][W];

	for(int i=0; i<H; i++) {
		for(int j=0; j<W; j++) {
			silk[i][j] = find_silk(map, H, W, i, j);
//			printf("%d ", silk[i][j]);
		}
//		printf("\n");
	}
//	printf("\n\n");

	std::map<int,char> basinmap;
	char c = 'a';
	int n;

	for(int i=0; i<H; i++) {
		for(int j=0; j<W; j++) {
			n = silk[i][j];
			if (basinmap.count(n) == 0) {
				basinmap[n] = c;
				c += 1;
			}

			printf("%c ", basinmap[n]);
		}
		printf("\n");
	}
}

int main() {
	int T;
	scanf("%d\n", &T);

	for(int i=0; i<T; i++) {
		printf("Case #%d:\n", i + 1);
		solve();
	}
}
