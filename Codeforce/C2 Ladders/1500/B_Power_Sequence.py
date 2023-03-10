import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

test_case = 1

#-------- DIFFERENT WAYS TO UNSTUCK ------------ 
# 1. Frequency/Value domain and Pigeon Hole Principle 
# 2. Search from end to start instead of start to end
# 3. Prefix Suffix
# 4. Brute force if small input size
def f(m):
    ans = 0
    for i, num in enumerate(A):
        ans += abs(m**i - num)
    return ans

def solve():
    A.sort()
    l = 0
    r = 10**9
    
    ans = 10**18
    x = 1
    while x**(n - 1) <=  f(1) + A[-1]:
        ans = min(ans, f(x))
        x += 1
    return ans
    

for _ in range(test_case):
    n = ri()
    A = ra()
    print(solve())