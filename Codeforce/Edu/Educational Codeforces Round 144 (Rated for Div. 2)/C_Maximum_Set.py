import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

test_case = ri()
mod = 998244353
#-------- DIFFERENT WAYS TO UNSTUCK ------------ 
# 1. Frequency/Value domain and Pigeon Hole Principle 
# 2. Search from end to start instead of start to end
# 3. Prefix Suffix
# 4. Brute force if small input size
def solve():
    ans = 0
    h = 0
    cur = L
    p = 1
    while cur <= R:
        cur *= 2
        p *= 2
        h += 1

    p = p//2

    ans = R//p
    ans = ans - L + 1

    if p >= 2:
        f = (p * 3)//2
        if f <= R/L:
            ans += (R//f - L + 1) * (h-1)
    return h, ans % mod

for _ in range(test_case):
    L, R = rmi()
    print(*solve())