import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))
mod = 998244353
n = ri()
a = ra()
l = []

ans = math.factorial(n//3)//(math.factorial(n//6)*math.factorial(n//6))
for i in range(0, n, 3):
	maxi = max(a[i] + a[i+1], a[i+1] + a[i+2], a[i] + a[i+2])
	count = ((a[i] + a[i+1]) == maxi) + ((a[i] + a[i+2]) == maxi) + ((a[i+1] + a[i+2]) == maxi)
	count %= mod
	ans *= count
print(ans%mod)



