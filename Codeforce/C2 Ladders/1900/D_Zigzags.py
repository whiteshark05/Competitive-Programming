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
    countLeft = [0] * (n + 1)
    ans = 0
    for j in range(n):
        countRight = [0] * (n + 1)
        for k in range(n-1, j, -1):
            ans += countLeft[A[k]] * countRight[A[j]]
            countRight[A[k]] += 1
        countLeft[A[j]] += 1
    return ans


for _ in range(test_case):
    n = ri()
    A = ra()
    print(solve())
