import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

inf = 10**18
test_case = 1

def solve():
    latest_startA, earliest_endA, latest_startB, earliest_endB = 0, inf, 0, inf
    #latest start time - earliest endtime
    for s, e in A:
        latest_startA = max(latest_startA, s)
        earliest_endA = min(earliest_endA, e)
    
    for s, e in B:
        latest_startB = max(latest_startB, s)
        earliest_endB = min(earliest_endB, e)
    
    ans = max(latest_startA - earliest_endB, latest_startB - earliest_endA)
    return ans if ans >= 0 else 0
    

for _ in range(test_case):
    n = ri()
    A, B = [], [] 
    for _ in range(n):
        s, e = rmi()
        A.append([s,e])
    m = ri()
    for _ in range(m):
        s, e= rmi()
        B.append([s,e])

    print(solve())