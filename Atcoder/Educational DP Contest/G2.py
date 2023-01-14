import sys
sys.setrecursionlimit(101010)

# DFS starting from toposorted vertices
nax = 10**5 + 5
dp = [0] * (nax) #DP is the longest path starting from vertex i
adj = [[] for i in range(nax)]



def dfs(u, p):
	if dp[u] != 0: return dp[u]	

	for v in adj[u]:
		if v != p:
			dp[u] = max(dp[u], dfs(v,u) + 1)

	return dp[u]

def solve():
	N, M = map(int, input().split())
	for i in range(M):
		u, v = map(int, input().split())
		u -= 1
		v -= 1
		adj[u].append(v)

	for i in range(N):
		dfs(i, -1)

	ans = 0
	for i in range(N):
		ans = max(ans, dp[i])
	return ans
print(solve())
