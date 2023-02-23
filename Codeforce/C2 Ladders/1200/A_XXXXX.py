import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

inf = 10**18
test_case = ri()

def solve():
    s = sum(A)
    if all (num % x  == 0 for num in A):
        return -1
    l, r = -1, -1
    if s % x:
        return n
    else:
        for i, num in enumerate(A):
            if num % x:
                if l == -1:
                    l = i 
                r = i
        # ----- (L - 1) -- L ---- (R - 1) --- R -------
        #segment 1: [L+1, N-1] -> length = (N - 1) - (L + 1) + 1 = N - L - 1 
        #segment 2: [0, R-1] -> length = (R - 1) - 0 + 1 = R
        return max(n - l - 1, r)
    


for _ in range(test_case):
    n, x  = rmi()
    A = ra()
    print(solve())