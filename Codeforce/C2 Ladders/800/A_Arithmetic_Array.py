import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

test_case = ri()

def solve():
    if sum(a) < len(a):
        return 1
    return abs(len(a) - sum(a))
    pass

for _ in range(test_case):
    n = ri()
    a = ra()
    print(solve())