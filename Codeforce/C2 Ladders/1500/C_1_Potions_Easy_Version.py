import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

test_case = 1

def solve():
    @functools.lru_cache(None)
    def dp(i, p):
        if i == N:
            return 0
        
        
    return dp(0,0)

for _ in range(test_case):
    N = ri()
    A = ra()
    print(solve())