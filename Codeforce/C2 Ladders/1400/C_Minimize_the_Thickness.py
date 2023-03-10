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

def go(i, target):
    if i == n: return 0
    cur = 0
    for j in range(i+1, n+1):
        cur += A[j-1]
        if cur > target: return n
        if cur == target:
            return max(j-i, go(j,target))
    return n
def solve():
    best = n
    curSum = 0
    for len in range(1, n):
        curSum += A[len - 1]
        best = min(best, go(0, curSum))
    return best
                

for _ in range(test_case):
    n = ri()
    A = ra()
    print(solve())