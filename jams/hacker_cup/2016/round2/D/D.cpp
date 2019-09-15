#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
#include <vector>
#include <set>

using namespace std;


void solve() {
	int N, K, P;
	scanf("%d %d %d\n", &N, &K, &P);
	printf("%d %d %d\n", N, K, P);
	int cost[N][K];

	for(int i=0; i<N; i++) {
		for(int j=0; j<K; j++) {
			cin >>cost[i][j];
		}
		scanf("\n");
	}

	/*
	for(int i=0; i<N; i++) {
		for(int j=0; j<K; j++) {
			cout <<"@ " <<cost[i][j];
		}
		cout <<endl;
	}
	*/

	vector<vector<int>> neig;
	int a,b;

	for(int i=0; i<N + 1; i++) {
		neig.push_back(vector<int>());
	}

	for(int i=1; i<N; i++) {
		scanf("%d %d\n", &a, &b);
		printf("-- %d %d\n", a, b);
		neig[a].push_back(b);
		neig[b].push_back(a);
	}
	
	int colors[N];
	for (int i=0; i<N; i++) colors[i] = 0;

	// Pick best colors
	for (int i=0; i<N; i++) {
		for (int j=0; j<K; j++) {
			int cc = colors[i];
			if (cost[i][j] < cost[i][cc]) {
			       	colors[i] = j;
			}
		}
	}

	int total_cost = 0;
	for (int i=0; i<N; i++) {
		int cc = colors[i];
		total_cost += cost[i][cc];
		
		bool pay = false;
		for (int& a : neig[i]) {
			for (int& b : neig[i]) {
				cout <<"? " <<a <<" " <<b;
				if (a != b && (colors[a] == colors[b])) {
					pay = true;
					break;
				}
			}
			cout <<endl;
//			if (pay) break;
		}

		if (pay) total_cost += P;
	}
	
	for (int i=0; i<N; i++) {
		cout <<colors[i] <<" ";
	}
	cout <<endl;

	cout <<total_cost <<endl;
}

int main() {
	int T;
	scanf("%d\n", &T);

	for(int i=0; i<T; i++) {
		printf("Case #%d:\n", i + 1);
		solve();
	}
}
