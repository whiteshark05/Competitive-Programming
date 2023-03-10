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
    for mask in range(1<<4):
        u, d, l, r = U, D, L ,R
        if mask & (1 << 0):
            l -= 1
            u -= 1
        
        if mask & (1 << 1):
            u -= 1
            r -= 1

        if mask & (1 << 2):
            r -= 1
            d -= 1

        if mask & (1 << 3):
            d -= 1
            l -= 1
        #print(bin(mask)[2:], u,r,d,l)
        if 0 <= u <= n - 2 and 0 <= d <= n-2 and 0 <= l <= n - 2 and 0 <= r <= n-2:
            return True
    return False



for _ in range(test_case):
    n, U, R, D, L = rmi()
    print('YES' if solve() else 'NO')