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
    freq = collections.Counter(s)
    even = 0
    odd = 0
    for f in freq.values():
        even += f//(2)
        odd += f%(2)

    q, r = divmod(even, k)
    odd += 2*r
    return 2*q + min(odd//k, 1)
    

for _ in range(test_case):
    n, k = rmi()
    s = rs()
    print(solve())