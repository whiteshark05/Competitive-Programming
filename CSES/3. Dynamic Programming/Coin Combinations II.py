import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

mod = 10**9+7

def solve():
    dp = [1] + [0] * (x) 
    for coin in coins:
        for i in range(coin, x + 1):        
            dp[i] += dp[i-coin]
            dp[i] %= mod           
    return dp[-1] % mod
    
n, x = rmi()
coins = ra()
print(solve())