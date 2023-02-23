import sys, math, itertools, functools, collections
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

n, m = rmi()
a = ra()

adj = [[] for _ in range(n)]
for u in a:
	adj[u-1].append(u)

vis = [False] * n 
ans = []

def dfs(u, path):
	vis[u] = True
	path.append(u+1)
	for v in adj[u]:
		if not vis[v]:
			dfs(v,path)
	return path

for i in range(n):
	if not vis[i]:
		ans += dfs(i,[])[::-1]
print(*ans)