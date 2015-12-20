#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
typedef long long ll;

void printEasyTest() {
    for (int i=1;i<=10000+rand()%1000;++i) cout << i << endl;
}

const ll MOD = 1000000000;

ll bigrand() {
    ll ret = (rand()*rand()*rand())%MOD;
    ret = (ret%MOD + MOD)%MOD;
    return ret;
}

void printHardTest() {
    for (int i=0;i<100000;++i) cout << 1+bigrand() << endl;
}

int main() {
    srand(time(NULL));
    //printEasyTest();
    printHardTest();
}