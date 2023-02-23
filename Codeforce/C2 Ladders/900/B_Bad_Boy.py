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
    x1, x2, x3, x4 = [(1,1), (1,n),(m,1),(m,n)]
    d1 = abs(x-1) + abs(y-1)
    d2 = abs(x-1) + abs(y-n)
    d3 = abs(x-m) + abs(y-1)
    d4 = abs(x-m) + abs(y-n)
    l = [(d1,x1),(d2,x2),(d3,x3),(d4,x4)]
    l.sort(reverse = True)
    ans = []
    for 
    return ans

for _ in range(test_case):
    m, n, x, y = rmi()
    print(*solve())

