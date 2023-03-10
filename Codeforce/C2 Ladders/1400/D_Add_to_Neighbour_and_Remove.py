import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

test_case = ri()

#-------- DIFFERENT WAYS TO UNSTUCK ------------ 
# 1. Frequency/Value domain and Pigeon Hole Principle 
# 2. Search from end to start instead of start to end
# 3. Prefix Suffix
# 4. Brute force if small input size

def solve():
    factors = []
    S = sum(A)
    for i in range(1,S+1):
        if S % i == 0:
            factors.append(i)
    best = n
    for target in factors:
        curSum = 0 
        k = 0
        ok = True
        for i in range(n):
            curSum += A[i]
            if curSum == target:
                k += 1
                curSum = 0
            elif curSum > target:
                ok = False
                break
        if ok:
            best = min(best, n - k)
        
    return best

for _ in range(test_case):
    n = ri()
    A = ra()
    print(solve())