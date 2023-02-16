import collections, heapq, itertools, math
groupby = itertools.groupby
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))
 
def solve():
    ans = set(a)
    return len(ans)
    
 
n = ri()
a = ra()
print(solve())