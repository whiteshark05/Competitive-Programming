import sys, math, itertools, functools, collections, heapq
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

test_case = ri()
inf = 10**18
#-------- DIFFERENT WAYS TO UNSTUCK ------------ 
# 1. Frequency/Value domain and Pigeon Hole Principle 
# 2. Search from end to start instead of start to end
# 3. Prefix Suffix
# 4. Brute force if small input size
def solve():
    #cur_max = -inf
    stack = []
    group = 0
    ans = 0
    h = []
    for i in range(n):
        if A[i] == 0:
            if h:
                ans += -heapq.heappop(h)
        else:
            heapq.heappush(h, -A[i])
    return ans
for _ in range(test_case):
    n =  ri()
    A = ra()
    print(solve())