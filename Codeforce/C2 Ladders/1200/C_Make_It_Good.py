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
    i = n - 1
    while i > 0 and A[i-1] >= A[i]:
        i -= 1

    while i > 0 and A[i-1] <= A[i]:
        i -= 1
    return i 
    

    pass

for _ in range(test_case):
    n = ri()
    A = ra()
    print(solve())