import collections, heapq, itertools, math
groupby = itertools.groupby
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

def solve():
    ans = []
    hi = n
    lo = 1
    j = 0
    
    player = 0
    while j < n:
        if player == 0:
            ans.append(hi)
            hi -= 1
        else:
            ans.append(lo)
            lo += 1
        j += 1
        player ^= 1
    return ans
    
for t in range(ri()):
    n, k = rmi()
    pa(solve())