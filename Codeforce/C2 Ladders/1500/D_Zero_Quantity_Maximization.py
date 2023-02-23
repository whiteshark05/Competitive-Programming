import sys, math, itertools, functools, collections
from fractions import Fraction
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

test_case = 1

def solve():
    freq = collections.Counter()
    special = 0

    for i in range(N):
        if A[i] == 0 and B[i] == 0:
            special += 1
        
        if A[i] != 0:
            freq[-Fraction(B[i])/Fraction(A[i])] += 1
    
    #print(freq)
    ans = 0
    for k, v in freq.items():
        ans = max(ans,v)
    return ans + special
    

for _ in range(test_case):
    N = ri()
    A = ra()
    B = ra()
    print(solve())