#include <algorithm>
#include <iostream>
#include <iomanip>
#include <unordered_set>
#include <utility>
#include <vector>
#include <math.h>

using namespace std;

typedef unordered_set<int> si;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<si> vsi;

struct point {
	int x, y;
};

struct drone_t {
	point pos;
	int space;
};

struct warehouse_t {
	point pos;
	vi products;
};

struct order_t {
	int id;
	bool done;
	point pos;
	vi products;
	vii list;
};

enum commands_type { load, unload, deliver, wait };

struct command_t {
	commands_type type;
	int drone;
	int a;
	int b;
	int c;
	point pos;
};

struct problem_t {
	int payload;
	int r, c;
	int turns;
	vi products;
	vector<drone_t> drones;
	vector<warehouse_t> warehouses;
	vector<order_t> orders;
	vector<command_t> commands;
};

void print_vi(const vi& v) {
    for (auto&& i : v) cout << i << " ";
    cout << endl;
}

void print_vvi(const vvi& v) {
    for (auto&& i : v) print_vi(i);
    cout << endl;
}

void print_vii(const vii& v) {
    for (auto&& i : v) cout << "<" << i.first << "," << i.second << "> ";
    cout << endl;
}

void print_problem(problem_t p) {
	cout <<p.r <<" x " <<p.c <<", " <<p.turns <<" turns" <<endl;
	cout <<"Products weight" <<endl;
	print_vi(p.products);
	cout <<"Warehouses" <<endl;
	for(auto & w : p.warehouses) {
		cout <<setw(4) <<w.pos.x <<", " <<setw(4) <<w.pos.y <<"    ";
		print_vi(w.products);
	}
	cout <<"Orders" <<endl;
	for(auto & o : p.orders) {
		cout <<setw(4) <<o.pos.x <<", " <<setw(4) <<o.pos.y <<"    ";
		for(int i = 0; i < o.products.size(); i++) {
			if (o.products[i]) {
				cout <<i <<": " <<o.products[i] <<" ";
			}
		}
		cout <<endl;
	}
}

void print_commands(problem_t p) {
	cout <<p.commands.size() <<endl;
	for(command_t & c : p.commands) {
		switch(c.type) {
			case load:
				printf("%d L %d %d %d\n", c.drone, c.a, c.b, c.c);
				break;
			case unload:
				printf("%d U %d %d %d\n", c.drone, c.a, c.b, c.c);
				break;
			case deliver:
				printf("%d D %d %d %d\n", c.drone, c.a, c.b, c.c);
				break;
		}
	}
}

int min(int a, int b) {	if (a < b) return a; else return b; }
int max(int a, int b) {	if (a > b) return a; else return b; }

int distance(point a, point b) {
	double x = a.x - b.x;
	double y = a.y - b.y;
	double dist = x*x + y*y;
//	dist = sqrt(dist);

    return ceil(dist);
}

int find_warehouse(problem_t &p, point pos, int type, int quantity) {
	int best = -1;
	double best_distance;

	for(int i = 0; i < p.warehouses.size(); i++) {
		warehouse_t & w = p.warehouses[i];

		if (w.products[type] >= quantity) {
			double d = distance(pos, w.pos);
			if ((best == -1) || d < best_distance) {
				best = i;
				best_distance = d;
			}
		}
	}

	if (best == -1) {
		cout <<"AAAAAAAAH" <<endl;
		exit(1);
	} else {
		return best;
	}
}

int order_cost(problem_t &p, order_t &order, point pos) {
	unsigned cost = 0;
	int total_q = 0;

	for(ii & o : order.list) {
		int type = o.first;
		int q = o.second;

		int w = find_warehouse(p, pos, type, q);
		cost += distance(pos, p.warehouses[w].pos);
		pos = p.warehouses[w].pos;

		// Load and deliver
		cost += 2;
		total_q += q;
	}

	cost += distance(pos, order.pos);

	return cost;
}

int best_order(problem_t &p, point pos) {
	int best = -1;
	double best_cost;

	for(int i = 0; i < p.orders.size(); i++) {
		order_t & order = p.orders[i];
		if (order.done) continue;

		double c = order_cost(p, order, pos);

		if ((best == -1) || c < best_cost) {
			best = i;
			best_cost = c;
		}
	}

	return best;
}

bool execute_order(problem_t &problem, int drone, order_t & order, auto & loads, auto & delivers) {
	for(ii & o : order.list) {
		int type = o.first;
		int & q = o.second;
		
		while (q) {
			int max_picked = (int) (problem.drones[drone].space / problem.products[type]);

			if (max_picked == 0) {
				// Full drone
				problem.drones[drone].space = problem.payload;
				return false;
			}

			int picked = min(max_picked, q);
			int where = find_warehouse(problem, problem.drones[drone].pos, type, picked);
			problem.drones[drone].pos = problem.warehouses[drone].pos;

			loads.push_back((struct command_t) {load, drone, where, type, picked, problem.warehouses[where].pos});
			delivers.push_back((struct command_t) {deliver, drone, order.id, type, picked, problem.orders[order.id].pos});

			q -= picked;
			problem.drones[drone].space -= picked * problem.products[type];
			problem.warehouses[where].products[type] -= picked;
			problem.drones[drone].pos = order.pos;
		}
	}

	order.done = true;
	return true;
}

int main(int argc, char* argv[]) {
	problem_t problem;

    int drones, types;
    cin >> problem.r >> problem.c >> drones >> problem.turns >> problem.payload >> types;

    for (int i = 0; i < types; i++) {
        int w;
        cin >> w;
		problem.products.push_back(w);
    }

    int w;
    cin >> w;

    for (int i = 0; i < w; i++) {
		warehouse_t warehouse;
        cin >> warehouse.pos.x >> warehouse.pos.y;
        for (int j = 0; j <types; j++) {
            int q;
            cin >> q;
			warehouse.products.push_back(q);
        }
		problem.warehouses.push_back(warehouse);
    }

    for (int i = 0; i < drones; i++) {
		drone_t drone;
		drone.pos = problem.warehouses[0].pos;
		drone.space = problem.payload;
		problem.drones.push_back(drone);
	}

    int o;
    cin >> o;
    for (int i = 0; i < o; i++) {
		order_t order;
		order.id = i;
        cin >> order.pos.x >> order.pos.y;
		order.products.assign(types, 0);

        int items;
        cin >> items;
        for (int j = 0; j < items; j++) {
            int item;
            cin >> item;
			order.products[item]++;
        }
		problem.orders.push_back(order);
    }
    
	for (int i = 0; i < o; i++) {
		order_t & order = problem.orders[i];
		order.done = false;

		for(int j = 0; j < types; j++) {
			if (order.products[j]) {
				order.list.push_back(make_pair(j, order.products[j]));
			}
		}
	}

	int drone = 1;
	int where = 1;

	vector<command_t> loads;
	vector<command_t> delivers;

	// Create an initial dispersion of the drones
	if (problem.warehouses.size() > 1) {
		for(drone = 1; drone < drones; drone++) {
			int i;
			for(i = 0; i < types; i++) if (problem.warehouses[0].products[i]) break;

			loads.push_back((struct command_t) {load, drone, 0, i, 1});
			delivers.push_back((struct command_t) {unload, drone, where, i, 1});

			problem.warehouses[0].products[i] -= 1;
			problem.drones[drone].pos = problem.warehouses[w].pos;
			where = (where + 1) % w;
		}

		problem.commands.insert(problem.commands.end(), loads.begin(), loads.end());
		problem.commands.insert(problem.commands.end(), delivers.begin(), delivers.end());

		loads.clear();
		delivers.clear();
	}


	while (true) {
		int order_id = best_order(problem, problem.drones[drone].pos);

		if (order_id == -1) {
			break;
		}

		order_t & order = problem.orders[order_id];
//		cout <<"Order " <<order_id <<" distance " <<distance(order.pos, problem.drones[drone].pos) <<endl;
		bool more_cargo = execute_order(problem, drone, order, loads, delivers);

		if (more_cargo) continue;

		auto command_comp = [&] (command_t a, command_t b) {
			double d1 = distance(a.pos, problem.drones[drone].pos);
			double d2 = distance(b.pos, problem.drones[drone].pos);
			return d1 < d2;
		};

		sort(begin(loads), end(loads), command_comp);
		sort(begin(delivers), end(delivers), command_comp);

		problem.commands.insert(problem.commands.end(), loads.begin(), loads.end());
		problem.commands.insert(problem.commands.end(), delivers.begin(), delivers.end());

		loads.clear();
		delivers.clear();
		drone = (drone + 1) % drones;
	}

	print_commands(problem);
}
