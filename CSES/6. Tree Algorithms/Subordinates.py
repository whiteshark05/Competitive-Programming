import sys, math, itertools, functools, collections
input = sys.stdin.readline

sys.setrecursionlimit(10**6)
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

n = ri()
a = ra()
adj = collections.defaultdict(list)
for u, v in enumerate(a):
	u += 2
	adj[v].append(u)
ans = [0] * n
def dfs(u, p):
	count = 0
	for v in adj[u]:
		if v == p: continue
		count += dfs(v,u)
		#print(count)
	ans[u-1] = count
	return count + 1


dfs(1,-1)

print(*ans)
#print(adj)