import sys, math, itertools, functools, collections
input = sys.stdin.readline

rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))
mod = 10**9+7

def solve():
    dp = [1] + [0] * (x) 
    for i in range(x + 1):
        for coin in coins:
            if i >= coin:
                dp[i] += dp[i-coin]
                dp[i] %= mod           
    return dp[-1] % mod
    
n, x = rmi()
coins = ra()
print(solve())

