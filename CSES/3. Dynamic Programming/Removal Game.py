import sys, math, itertools, functools, collections
input = sys.stdin.readline
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

n = ri()
a = ra()
s = sum(a)
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
	dp[i][i] = a[i]

for l in range(n-1, -1, -1):
	for r in range(l+1, n):
		dp[l][r] = max(a[l] - dp[l+1][r], a[r] - dp[l][r-1])

print((s + dp[0][-1])//2)