import collections, heapq, itertools, math
groupby = itertools.groupby
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))
mod = 10**9+7
inf = 10**9

def solve():
    dp = [[0] * n for _ in range(n)]

    

    #print(dp)
    return dp[-1][-1] % mod
    
n, x = rmi()
h = ra()
s = ra()
print(solve())