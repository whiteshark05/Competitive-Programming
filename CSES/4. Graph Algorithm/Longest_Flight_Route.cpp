#include <bits/stdc++.h>
using namespace std;
int n,m,x,y,dp[100010];
vector<int> ts, adj[100010], r_adj[100010], p(100010);
bool vis[100010];
stack<int> S;
 
void dfs(int s)
{
    vis[s]=true;
    for(auto u : adj[s])
        if(!vis[u]) dfs(u);
    ts.push_back(s);
}
 
int32_t main()
{
    cin >> n >> m;
    for(int i = 0; i < m; i++)
    {
        cin >> x >> y;
        adj[x].push_back(y);
        r_adj[y].push_back(x);
    }
    dfs(1), dp[1]=1, p[1]=-1, reverse(ts.begin(), ts.end());
    for(auto u : ts){
        //cout << u << ' ';
        for(auto v : r_adj[u]){
            cout << u-1 << ' ' << v-1 << '\n';
            if(u>1 and dp[u]<dp[v]+1)
            	dp[u] = dp[v]+1, p[u]=v;
        }
    }
	if(!dp[n]){cout<<"IMPOSSIBLE"; return 0;}
    cout << dp[n] << "\n"; x=n;
    while(x!=-1) S.push(x), x=p[x];
    while(!S.empty()){
    	cout << S.top() << " "; S.pop();
    }
}