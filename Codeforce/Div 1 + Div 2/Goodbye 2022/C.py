import collections, heapq, itertools, math
from math import gcd
groupby = itertools.groupby
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
 
def solve(n,a):
    g = a[0]
    for i in range(1, n):
        g = gcd(g, a[i])
    if g != 1:
        return False
    for i in range(n):
        for j in range(i+1, n):
            if gcd(a[i]+g, a[j]+g) == 1:
                return False
    return True
    
 
for t in range(ri()):
    n = ri()
    a = ra()
    print("YES" if solve(n,a) else "NO")