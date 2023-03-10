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
 
void solve(){
    int n, x;
    cin >> n >> x;
    map<int,int> m;
    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;
        if (m.find(x - tmp) != m.end()){
            cout << m[x - tmp] << ' ' << i + 1;
            exit(0);
        }

        m[tmp] = i + 1;
    }

    cout << "IMPOSSIBLE";

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