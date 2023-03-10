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

def solve(h,p):
    x = int(math.log2(p))
    have = 2**h - 1
    ready = 1
    ans = 0
    while have > 0:
        have -= ready
        ans += 1
        ready *= 2
        if ready >= p:
            break
    return ans + int(math.ceil(have/p))

for _ in range(test_case):
    h, p = rmi()
    print(solve(h,p))
