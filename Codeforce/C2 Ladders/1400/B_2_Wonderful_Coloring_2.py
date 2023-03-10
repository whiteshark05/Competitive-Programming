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
    freq = collections.Counter(A)
    usable = 0
    ans = 0
    for num, v in freq.items():
        if v >= k:
            ans += v//k
        else:
            usable += v
    #print(usable)
    if usable >= k:
        ans += 1
    return ans
    
for _ in range(test_case):
    n, k = rmi()
    A = ra()
    print(solve())