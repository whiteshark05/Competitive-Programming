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
    a, b, c, d = A
    if a < b:
        a, b = b, a

    if c < d:
        c, d = d, c
    
    if a > c:
        return c > b
    else:
        return a > d

for _ in range(test_case):
    A = ra()
    print('YES' if solve() else 'NO')