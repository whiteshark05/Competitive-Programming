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
    A.sort()
    ans = []

    if n == 2:
        return A

    pos, mn = -1, 10**18
    for i in range(1,n ):
        if mn > abs(A[i] - A[i-1]):
            pos = i
            mn = abs(A[i] - A[i-1])
            
    #print(pos)
    
    for i in range(pos, n):
        ans.append(A[i])
    
    for i in range(pos):
        ans.append(A[i])
    return ans



for _ in range(test_case):
    n = ri()
    A = ra()
    print(*solve())