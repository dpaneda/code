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

int calculate_rough(list<unsigned int> L, unsigned int size, unsigned int distance) {
	unsigned int actual, sum = 0;
	int partial;
    list<unsigned int>::iterator li;
    li = L.begin();
    actual = *li;
    ++li;
    for (; li != L.end(); ++li) {
    	partial = actual - *li;
    	partial = abs(partial) - distance;
		if (partial > 0)
			sum += partial;
		actual = *li;
	}
	return sum;
}

void testcase(short index) {
	unsigned int val, i, cost=0;
    unsigned int D,I,M,N;
    unsigned int roughness, min_roughness, tmp_roughness;

    cin >> D >>I >>M >>N;

    list<unsigned int> L;
    for (i = 0; i < N; i++) {
        cin >> val;
        L.push_back(val);
    }

    //cout <<D <<" " <<I <<" " <<M <<" " <<N <<endl;
    list<unsigned int>::iterator li;
    for (li = L.begin(); li != L.end(); ++li)
    	cout << *li << " ";
    cout << endl;

    roughness = calculate_rough(L, N, M);
    cout <<roughness <<endl;

    if (roughness >= 0) {
    	cout << "Case #" << index + 1 << ": " <<cost <<endl;
    }

   /* for (i = 0; i < N; i++ ) {

    	tmp_roughness = calculate_rough(val, N, M);
    }*/
}
