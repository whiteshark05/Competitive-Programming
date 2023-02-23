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
    L = [(v,i) for i,v in enumerate(A)]
    L.sort()
    ans = 1
    for i in range(1,n):
        if L[i-1][1] + 1 != L[i][1]:
            ans += 1
    return ans <= k


for _ in range(test_case):
    n, k = rmi()
    A = ra()
    print('Yes' if solve() else 'No')