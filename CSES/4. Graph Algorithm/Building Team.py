import sys, math, itertools, functools, collections
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))


n, m = rmi()
adj = [[] for _ in range(n)]

for _ in range(m):
	u, v  = rmi()
	u -=  1
	v -= 1
	adj[u].append(v)
	adj[v].append(u)

color = [-1]*n
ok = True

stack = []
c = 0

def dfs(u, c):
	if color[u] == c: return True
	if color[u] == 1 - c: return False
	color[u] = c
	for v in adj[u]:
		if not dfs(v, 1-c):
			return False
	return True

for i in range(n):
	if color[i] == -1 and not dfs(u,c):
		ok = False
		break
print(color)
if not ok:
	print('IMPOSSIBLE')
	exit()
else:
	print(*color)


