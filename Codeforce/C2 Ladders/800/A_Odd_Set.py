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
    count = 0
    for num in a:
        if num % 2 == 1:
            count += 1
    return count == len(a) - count
    pass
for _ in range(test_case):
    n = ri()
    a = ra()
    print('Yes' if solve() else 'No')