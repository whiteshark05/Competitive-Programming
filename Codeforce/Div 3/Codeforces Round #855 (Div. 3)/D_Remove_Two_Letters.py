import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

test_case = ri()

@functools.lru_cache(maxsize=None)
def ncr(n, r):
    r = min(r, n-r)
    numer = itertools.reduce(op.mul, range(n, n-r, -1), 1)
    denom = itertools.reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2

#-------- DIFFERENT WAYS TO UNSTUCK ------------ 
# 1. Frequency/Value domain and Pigeon Hole Principle 
# 2. Search from end to start instead of start to end
# 3. Prefix Suffix
# 4. Brute force if small input size
def solve():
    ans = n - 1
    for i in range(2, n):
        ans -= s[i-2] == s[i]
    return ans
    

for _ in range(test_case):
    n = ri()
    s = rs()
    print(solve())