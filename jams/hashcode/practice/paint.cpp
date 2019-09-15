#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include "boost/multi_array.hpp"

using namespace std;

enum Command { paint_square, erase_cell, paint_line };

struct cmd_t {
	Command type;
	int a,b,c,d;
};

typedef boost::multi_array<int, 2> grid_t;
typedef grid_t::index index;

void print_cmds(vector<cmd_t> cmds) {
	cout <<cmds.size() <<endl;
	for (cmd_t & cmd : cmds) {
		switch (cmd.type) {
			case paint_square:
				printf("%s %d %d %d\n", "PAINT_SQUARE", cmd.a, cmd.b, cmd.c);
				break;
			case erase_cell:
				printf("%s %d %d\n", "ERASE_CELL", cmd.a, cmd.b);
				break;
			case paint_line:
				printf("%s %d %d %d %d\n", "PAINT_LINE", cmd.a, cmd.b, cmd.c, cmd.d);
				break;
		}
	}
}

vector<cmd_t> get_raster_cmds (auto &grid, int N, int M) {
	vector<cmd_t> cmds;

	int painting = 0;
	int i,j,x1,y1;

	
	for(i=0; i<N; i++) {
		for(j=0; j<M; j++) {
			if (painting != grid[i][j]) {
				if (painting) {
					cmd_t c = {paint_line, x1, y1, i, j - 1};
					cmds.push_back(c);
					painting = 0;
				} else {
					painting = 1;
					x1 = i;
					y1 = j;
				}
			}
		}
		if (painting) {
			cmd_t c = {paint_line, x1, y1, i, j - 1};
			cmds.push_back(c);
			painting = 0;
		}
	}

	return cmds;
}

int get_square_gaps(auto &grid, int x, int y) {
	int clear = 0;

	for(int i = y - 1; i <= y + 1 ; i++) {
		for(int j = x - 1; j <= x + 1; j++) {
			if (! grid[i][j]) {
				clear++;
			}
		}
	}

	return clear;
}

vector<cmd_t> get_square_cmds (auto &grid, int N, int M) {
	vector<cmd_t> cmds;

	int i,j,x1,y1;
	
	for(i=1; i < N - 1; i++) {
		for(j=1; j < M - 1; j++) {
			if (get_square_gaps(grid, j, i) > 0) {
				continue;
			}
			
			cmd_t c = {paint_square, i, j, 1};
			cmds.push_back(c);

			for(int a = i - 1; a <= i + 1 ; a++) {
				for(int b= j - 1; b <= j + 1; b++) {
					if (! grid[a][b]) {
						cmd_t c = {erase_cell, a, b};
						cmds.push_back(c);
					}
				}
			}
		}
	}

	return cmds;
}

vector<cmd_t> get_vraster_cmds (auto &grid, int N, int M) {
	vector<cmd_t> cmds;

	int painting = 0;
	int i,j,x1,y1;
	
	for(j=0; j<M; j++) {
		for(i=0; i<N; i++) {
			if (painting != grid[i][j]) {
				if (painting) {
					cmd_t c = {paint_line, y1, x1, i - 1, j};
					cmds.push_back(c);
					painting = 0;
				} else {
					painting = 1;
					y1 = i;
					x1 = j;
				}
			}
		}
		if (painting) {
			cmd_t c = {paint_line, y1, x1, i - 1, j};
			cmds.push_back(c);
			painting = 0;
		}
	}

	return cmds;
}

int max(int a, int b) {
	return (a > b) ? a : b;
}

int cmd_size(cmd_t c) {
	return max(c.c - c.a, c.d - c.b);
}

void paint(grid_t & grid, cmd_t c) {
	if (c.type == paint_line) {
		if (c.c != c.a) {
			int d = c.c - c.a;
			for (int i=0; i <= d; i++) {
				grid[c.a + i][c.b] = 0;
			}
		} else {
			int d = c.d - c.b;
			for (int i=0; i <= d; i++) {
				grid[c.a][c.b + i] = 0;
			}
		}
	} else if (c.type == paint_square) {
		for (int i = c.a - 1; i <= c.a + 1; i++) {
			for (int j = c.b - 1; j <= c.b + 1; j++) {
				grid[i][j] = 0;
			}
		}
	}
}

int painted(grid_t & grid, cmd_t c) {
	int painted = 0;

	if (c.type == paint_line) {
		if (c.c != c.a) {
			int d = c.c - c.a;
			for (int i=0; i <= d; i++) {
				painted += grid[c.a + i][c.b];
			}
		} else {
			int d = c.d - c.b;
			for (int i=0; i <= d; i++) {
				painted += grid[c.a][c.b + i];
			}
		}
	} else if (c.type == paint_square) {
		for (int i = c.a - 1; i <= c.a + 1; i++) {
			for (int j = c.b - 1; j <= c.b + 1; j++) {
				painted += grid[i][j];
			}
		}
	} else if (c.type == erase_cell) {
		return -1;
	}

	return painted;
}

class cmd_cmp {
	grid_t & grid;
	public:

	cmd_cmp(grid_t &g) : grid(g) {}

	bool operator() (cmd_t c1, cmd_t c2) {
		int l1 = painted(grid, c1);
		int l2 = painted(grid, c2);

		return l1 < l2;
	}
};

int main() {
	int N, M;
	scanf("%d %d\n", &N, &M);

	grid_t grid(boost::extents[N][M]);

	std::string line;
	int to_paint = 0;

	for(int i=0; i<N; i++) {
		std::getline(std::cin, line);
		for(int j=0; j<M; j++) {
			if (line[j] == '#') {
				grid[i][j] = 1;
				to_paint++;
			}
		}
	}

/*
	cout <<N <<" " <<M <<" " <<to_paint <<endl;
	for(int i=0; i<N; i++) {
		for(int j=0; j<M; j++) {
			cout <<((grid[i][j] == 1) ? 'X': '.');
		}
		cout <<endl;
	}
*/
	vector<cmd_t> square_cmds = get_square_cmds(grid, N, M);

/*
	to_paint = 0;
	for(int i=0; i<N; i++) {
		for(int j=0; j<M; j++) {
			if (grid[i][j]) {
				to_paint++;
			}
		}
	}
*/
//	cout <<to_paint <<endl;

	vector<cmd_t> cmds = get_raster_cmds(grid, N, M);
	vector<cmd_t> v_cmds = get_vraster_cmds(grid, N, M);

	cmds.insert(cmds.end(), v_cmds.begin(), v_cmds.end());
	cmds.insert(cmds.end(), square_cmds.begin(), square_cmds.end());

	vector<cmd_t> final_cmds;
	cmd_t cmd;

	while (to_paint > 0) {
		sort(cmds.begin(), cmds.end(), cmd_cmp(grid));
		cmd = cmds.back();
		cmds.pop_back();
		final_cmds.push_back(cmd);
		to_paint -= painted(grid, cmd);
		paint(grid, cmd);
	}

	print_cmds(final_cmds);
}
