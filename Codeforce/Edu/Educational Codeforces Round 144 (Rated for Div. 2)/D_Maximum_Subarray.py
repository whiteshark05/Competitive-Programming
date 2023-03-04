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
    l = 0
    cur = 0
    ans = 0
    for r in range(len(A)):
        cur += A[r]
        if r - l + 1 > n - k:
            cur -= A[l]
        ans = max(ans, cur + )
    return ans

for _ in range(test_case):
    n, k, x = rmi()
    A = ra()
    print(solve())