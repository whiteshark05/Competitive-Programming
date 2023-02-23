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
    if a == b:
        return 0
    elif abs(b - a) >= x:
        return 1
    elif (abs(r - a) >= x and abs(r - b) >= x) or (abs(a - l) >= x and abs(b - l) >= x):
        return 2
    elif (abs(a - l) >= x and abs(r - b) >= x) or (abs(r - a) >= x and abs(b - l) >= x):
        return 3
    return -1


for _ in range(test_case):
    l, r, x = rmi()
    a, b = rmi()
    print(solve())