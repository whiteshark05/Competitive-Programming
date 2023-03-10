import sys, math, itertools, functools, collections, heapq
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
    
    ans = []
    h = []
    for i in range(1,n):
        if A[i-1] > A[i]:
            heapq.heappush(h,(A[i-1]-A[i], i))
    if not h:
        return [1] * n
    add = 1
    while h:
        d, i = heapq.heappop(h)
        A[i] += add
        ans.append(i+1)
        if len(ans) == n:
            break
        add += 1
        heapq.heappush(h,(d-add,i))
    
    return ans
    pass

for _ in range(test_case):
    n = ri()
    A = ra()
    print(*solve())