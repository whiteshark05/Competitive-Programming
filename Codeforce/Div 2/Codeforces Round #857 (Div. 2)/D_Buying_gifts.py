import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))
inf = 10**18
test_case = ri()

#-------- DIFFERENT WAYS TO UNSTUCK ------------ 
# 1. Frequency/Value domain and Pigeon Hole Principle 
# 2. Search from end to start instead of start to end
# 3. Prefix Suffix
# 4. Brute force if small input size

def solve():
    l = sorted(zip(A,B))
    sortedA = [x[0] for x in l]
    sortedB = [x[1] for x in l]
    #print(sortedA, sortedB)
    left, right = [inf], [-inf] # min value on the left/right of i
    for i in range(n-1):
        left.append(min(left[-1],sortedB[i]))
    
    invB = sortedB[::-1]
    for i in range(n-1):
        right.append(max(right[-1],invB[i]))
    right = right[::-1]
    #print(left, right)

    ans = inf
    for i in range(n):
        cand = min(left[i],right[i] if right[i] != -inf else inf)
        d = abs(sortedA[i] - cand)
        ans = min(ans, d)
        #print(sortedA[i], left[i], right[i])
    return ans

for _ in range(test_case):
    A, B = [], []
    n = ri()
    for _ in range(n):
        a, b = rmi()
        A.append(a)
        B.append(b)
    print(solve())