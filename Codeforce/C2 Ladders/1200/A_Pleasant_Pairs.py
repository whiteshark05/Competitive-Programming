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
    for i in range(n-1):
        for j in range(i+1, n):
            if i + j + 2 == A[i] * A[j]:
                count += 1
    return count

for _ in range(test_case):
    n = ri()
    A = ra()
    print(solve())