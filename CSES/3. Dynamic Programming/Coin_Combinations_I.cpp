#include <bits/stdc++.h>
#define all(x) begin(x),end(x)
#define fir first
#define sec second
#define sz(x) x.size()
#define pb push_back
 
using namespace std;
using ll = long long;
using vi = vector<int>;
using pi = pair<int,int>;
using pdb = pair<double,double>;
using pll = pair<ll,ll>;
using vll = vector<ll>;
using ull = unsigned long long;
const double EPS = (1e-6);

void setio(string s){
    freopen((s + ".in").c_str(),"r",stdin);
    freopen((s + ".out").c_str(),"w",stdout);
}

ll dp[1000001];

const int MOD = (int)1e9 + 7;
 
void solve(){
    int n;
    ll x;
    cin >> n >> x;

    vll dp(x+1);
    dp[0] = 1;
    vll coins(n);
    for (int i = 0; i < n; ++i){
        cin >> coins[i] ;
    }

    for (int i = 0; i <= x; ++i){
        for (auto coin:coins){
            if (i >= coin){
                dp[i] += dp[i-coin];
                dp[i] %= MOD;
            }
        }
    }

    cout << dp[x] % MOD << '\n';
}
 
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    //cin >> t;
    while(t--){
        solve();
    }
    return 0;
}