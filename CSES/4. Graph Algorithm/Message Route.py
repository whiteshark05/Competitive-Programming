import sys, math, itertools, functools, collections
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

n, m = rmi()
adj = [[] for _ in range(n+1)]
for _ in range(m):
	u, v = rmi()
	adj[u].append(v)
	adj[v].append(u)
 
step = 1
cur_level = [(1,[1])]
seen = set({1})
while cur_level:
	next_level = []
	for cur, path in cur_level:
		for nxt in adj[cur]:
			if nxt == n:
				print(step + 1)
				print(*(path[:] + [n]))
				exit()
			if nxt not in seen:
				seen.add(nxt)
				next_level.append((nxt, path + [nxt]))
	cur_level = next_level
	step += 1
print('IMPOSSIBLE')
