import sys
sys.setrecursionlimit(101010)

# DFS starting from toposorted vertices
nax = 10**5 + 5
dp = [0] * (nax) #DP is the longest path starting from vertex i
adj = [[] for i in range(nax)]
visited = [False] * (nax)
indegree = [0] * (nax) #number of edges going to v

def dfs(u):
	visited[u] = True

	for v in adj[u]:
		dp[v] = max(dp[v], 1 + dp[u])
		indegree[v] -= 1

		if indegree[v] == 0:
			dfs(v)

def solve():
	N, M = map(int, input().split())
	for i in range(M):
		u, v = map(int, input().split())
		u -= 1
		v -= 1
		adj[u].append(v)
		indegree[v] += 1

	for i in range(N):
		if visited[i] == False and indegree[i] == 0:
			dfs(i)

	ans = 0
	for i in range(N):
		ans = max(ans, dp[i])
	return ans
print(solve())



import collections, heapq, itertools, math

rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

def solve():
    ans = 
    return ans
    
for t in range(ri()):
    
    print(solve())
