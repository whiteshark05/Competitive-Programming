import collections, heapq, itertools, math
groupby = itertools.groupby
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))
mod = 10**9+7
inf = 10**9
"""
4
....  1 1 1 1
.*..  1 0 1 1
...*  1 1 2 0
*...  0 1 3 3

"""
def solve():
    dp = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            if r == 0 and c == 0:
                dp[r][c] = a[r][c] == '.'
                continue
            if a[r][c] == '.':
                dp[r][c] = (dp[r-1][c] if r > 0 else 0) + (dp[r][c-1] if c > 0 else 0)
            else:
                dp[r][c] = 0

    #print(dp)
    return dp[-1][-1] % mod
    
n = ri()
a = []
for _ in range(n):
    a.append(list(rs()))

print(solve())