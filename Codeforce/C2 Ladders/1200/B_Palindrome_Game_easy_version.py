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
    count = s.count('0')
    if count == 1 or count % 2 == 0:
        return 'BOB'
    return 'ALICE'
    pass

for _ in range(test_case):
    n = ri()
    s = rs()
    print(solve())