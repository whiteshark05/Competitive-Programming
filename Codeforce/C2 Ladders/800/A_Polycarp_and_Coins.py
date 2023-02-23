import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]

test_case = ri()
def solve():
    if n % 3 == 0:
        return [n//3, n//3]
    elif n % 3 == 1:
        return [n//3+1, n//3]
    else:
        return [n//3,n//3+1]

    
for _ in range(test_case):
    n = ri()
    print(*solve())
