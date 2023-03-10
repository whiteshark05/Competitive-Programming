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
    # Dealing with negatives
    # Dealing with duplicates
    pos = sorted([x for x in A if x >= 0])
    neg = sorted([x for x in A if x <0])
    
    i = len(pos) - 1
    ans = 0
    while i >= 0:
        ans += pos[i] * 2
        i -= k
    
    j = 0
    while j < len(neg):
        ans += abs(neg[j]) * 2
        j += k
    return ans - max(pos[-1] if pos else 0, abs(neg[0]) if neg else 0)




for _ in range(test_case):
    n, k = rmi()
    A = ra()
    print(solve())