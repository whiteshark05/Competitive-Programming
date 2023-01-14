import collections, heapq, itertools, math
groupby = itertools.groupby
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

def solve():
    ans = sum(x % 2 == 1 for x in a)
    return ans
    
for t in range(ri()):
    n = ri()
    a = ra()

    print(solve())