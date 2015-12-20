#include <iostream>
using namespace std;
typedef long long ll;

const ll MOD = 3211123;
/*
//calc function exactly as it is in the problem statement.
long long calc(int n){
    long long ret = 0,a,b,c,d,e,f,g,M = 3211123;
    for(a = 1; a <= n; a++)
        for(b = 1; b <= n; b++)
            for(c = 1; c <= n; c++)
                for(d = 1; d <= n; d++)
                    for(e=1; e <= n; e++)
                        for(f=1; f <= n; f++)
                            for(g=1; g <= n; g++)
                                if(a + b + c + d + e + f + g == n)
                                    ret = (ret + a*a + b*b + c*c + d*d + e*e + f*f + g*g)%M;

    return ret;
}
*/
//Returns a to the b-th power.
ll pot(ll a, ll b) {
    if (b==0) return 1;
    ll x = pot(a, b/2);
    x = (x*x)%MOD;
    if (b&1) x = (x*a)%MOD;
    return x;
}

//Returns b such that a*b = 1 (mod MOD)
ll inv(ll a) {
    return pot(a, MOD-2);
}

//Returns x^8/2880-x^7/120+(119 x^6)/1440-(7 x^5)/16+(3829 x^4)/2880-(553 x^3)/240+(167 x^2)/80-(3 x)/4 (mod MOD)
ll fastCalc(ll x) {
    ll ans = 0;
    ans = (ans + pot(x,8)*inv(2880))%MOD;
    ans = (ans - pot(x,7)*inv(120))%MOD;
    ans = (ans + 119*pot(x,6)*inv(1440))%MOD;
    ans = (ans - 7*pot(x,5)*inv(16))%MOD;
    ans = (ans + 3829*pot(x,4)*inv(2880))%MOD;
    ans = (ans - 553*pot(x,3)*inv(240))%MOD;
    ans = (ans + 167*pot(x,2)*inv(80))%MOD;
    ans = (ans - 3*x*inv(4))%MOD;
    
    //Make the number positive
    ans = (ans%MOD + MOD)%MOD;
    return ans;
}

int main() {
    ll n; //1<=n<=10^9
    while(cin>>n) cout << fastCalc(n) << endl;
}
