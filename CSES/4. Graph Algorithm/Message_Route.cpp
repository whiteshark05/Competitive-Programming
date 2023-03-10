#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define ld long double
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define sz(x) (int)(x).size()
#define rep(i,a,b) for(int i=(a);i<=(b);i++)
#define per(i,b,a) for(int i=(b);i>=(a);i--)
#define all(x) (x).begin(), (x).end()

template<typename T> bool chkMax(T&x, T y) { return (y>x)?x=y, 1:0; }
template<typename T> bool chkMin(T&x, T y) { return (y<x)?x=y, 1:0; }

template<typename T> void inline read(T&x){
    x=0;char c=getchar();bool flag=false;
    while(!isdigit(c)){if(c=='-')flag=true;c=getchar();}
    while(isdigit(c)){x=(x<<1)+(x<<3)+(c^48);c=getchar();}
    if(flag) x=-x;
}

const int MAXN = 1e6+5;
const int INF = 0x3f3f3f3f;

int n, m;
vector<int> adj[MAXN];

int main(){
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    cin >> n >> m;
    rep(i,1,m){
        int u, v; cin >> u >> v;
        adj[u].pb(v);
        adj[v].pb(u);
    }
    int step = 1;
    vector<pair<int,vector<int>>> cur_level = {{1,{1}}};
    set<int> seen = {1};
    while(!cur_level.empty()){
        vector<pair<int,vector<int>>> next_level;
        for(auto [cur, path] : cur_level){
            for(auto nxt : adj[cur]){
                if(nxt == n){
                    cout << step+1 << "\n";
                    path.pb(n);
                    for(auto x : path)
                        cout << x << " ";
                    cout << "\n";
                    return 0;
                }
                if(!seen.count(nxt)){
                    seen.insert(nxt);
                    path.pb(nxt);
                    next_level.pb({nxt,path});
                    path.pop_back();
                }
            }
        }
        cur_level = next_level;
        step++;
    }
    cout << "IMPOSSIBLE\n";
    return 0;
}