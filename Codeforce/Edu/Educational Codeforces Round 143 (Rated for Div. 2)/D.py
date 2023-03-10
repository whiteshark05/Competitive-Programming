import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)
"""
def ncr(n, r, p):
 
    num = den = 1 
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p
"""
rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))
t = 1
def solve():
	pass
	
for _ in range(t):
	print(solve())
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



