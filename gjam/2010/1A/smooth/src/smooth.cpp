#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <list>

using namespace std;

void testcase(short index);

int main(int argc, char** argv) {
    int tests ;
    cin >> tests;
    for (int i = 0; i < tests; i++) {
        testcase(i);
    }

    return 0;
}

int abs(int a) {
	return (a > 0) ? a : -a;
}

class RoughVector:public list<unsigned int>
{
	private:
		unsigned int size, distance, delete_cost, insert_cost, cost, step_cost;

	public:
		RoughVector::iterator li, peak;
		RoughVector(unsigned int _delete_cost, unsigned int _insert_cost,
				unsigned int _distance, unsigned int _size) {
			cost = 0;
			size = _size;
			distance = _distance;
			delete_cost =_delete_cost;
			insert_cost = _insert_cost;
			if (delete_cost > insert_cost)
				step_cost = delete_cost;
			else
				step_cost = insert_cost;
		}

		RoughVector & operator=(const RoughVector &that) {
			list<unsigned int>::operator=(that);
			size = that.size;
			distance = that.distance;
			delete_cost = that.delete_cost;
			insert_cost = that.delete_cost;
			cost = that.cost;
			step_cost = that.cost;
			return *this;
	    }


		int calculate_rough() {
			unsigned int actual, sum = 0;
			int partial;
			if (size < 2)
				return 0;
			li = begin();
			actual = *li;
			++li;
			for (; li != end(); ++li) {
				partial = actual - *li;
				partial = abs(partial) - distance;
				if (partial > 0)
					sum += partial;
				actual = *li;
			}
			return sum;
		}

		RoughVector::iterator get_highest_peak() {
			RoughVector::iterator prev, actual, next;
			unsigned int max, tmp;

			if (size < 3)
				return begin();
			li = begin();
			prev = li;
			++li;
			actual = li;
			++li;
			max = 0;
			for (; li != end(); ++li) {
				next = li;
				tmp = abs(static_cast<int>(*actual - *prev));
				tmp = abs(static_cast<int>(*next - *actual));

				if (tmp > max) {
					max = tmp;
					peak = actual;
				}

				prev++;
				actual++;
			}

			return peak;
		}

		int optimal_delete_improvement() {
			RoughVector v = *this;
			v.delete(get_highest_peak());
			return v.calculate_rough();
		}

		void improve() {
			int d, i, m;
			d = optimal_delete_improvement();
			cout <<d;
		}
};

void testcase(short index) {
	unsigned int val, i, cost=0;
    unsigned int D,I,M,N;
    unsigned int roughness;

    cin >> D >>I >>M >>N;

    RoughVector L(D,I,M,N);
    for (i = 0; i < N; i++) {
        cin >> val;
        L.push_back(val);
    }

    //cout <<D <<" " <<I <<" " <<M <<" " <<N <<endl;
    RoughVector::iterator li;
    for (li = L.begin(); li != L.end(); ++li)
    	cout << *li << " ";
    cout << endl;

    roughness = L.calculate_rough();
    cout <<roughness <<endl;

    if (roughness >= 0) {
    	cout << "Case #" << index + 1 << ": " <<cost <<endl;
    }

    L.get_highest_peak();
    cout <<*L.peak <<endl;

    L.improve();
/*
    for (li = L.begin(); li != L.end(); ++li) {

    	tmp_roughness = calculate_rough();
    }*/
}
