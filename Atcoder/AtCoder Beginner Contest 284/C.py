import collections, heapq, itertools, math
groupby = itertools.groupby
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))


n, m = rmi()
adj = collections.defaultdict(list)
parent = [i for i in range(n)]
def find(u):
	if parent[u] == u:
		return u 
	parent[u] = find(parent[u])
	return parent[u]

def union(u,v):
	pu, pv = find(u), find(v)
	if pu != pv:
		parent[pu] = pv
    
for _ in range(m):
	u, v = rmi()
	u -= 1
	v -= 1
	union(u,v)

ans = 0
for i in range(n):
	if find(i) == i:
		ans += 1

print(ans)