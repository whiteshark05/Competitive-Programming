import sys, math, itertools, functools, collections
input = sys.stdin.readline
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

n = ri()
a = ra()
count = collections.defaultdict(int)
ans = 0
l = 0
for r in range(n):
	l = max(count[a[r]], l)
	ans = max(ans, r - l + 1)
	count[a[r]] = r + 1
	print(r, l, count)
print(ans)