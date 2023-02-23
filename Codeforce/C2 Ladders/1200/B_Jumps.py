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
    i = 1
    while i*(i+1) < 2*n:
        i += 1
    if i*(i+1)//2 == n + 1:
        i += 1
    return i
    pass

for _ in range(test_case):
    n = ri()
    print(solve())