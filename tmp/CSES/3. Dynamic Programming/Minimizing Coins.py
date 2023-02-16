import collections, heapq, itertools, math
groupby = itertools.groupby
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))
inf = 10**18
def solve():
    dp = [inf] * (x+1)
    dp[0] = 0
    for coin in a:
    	for i in range(coin, x + 1):
    		dp[i] = min(dp[i], 1 + dp[i-coin])

    #print(dp)
    return dp[-1] if dp[-1] != inf else -1
    
n, x = rmi()
a = ra()
print(solve())