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
    if A[0] == 1:
        A[0] += 1

    for i in range(1, n):
        if A[i] == 1:
            A[i] += 1
        if A[i] % A[i-1] == 0:
            A[i] += 1
    return A



for _ in range(test_case):
    n = ri()
    A = ra()
    print(*solve())


import sys, math, itertools, functools, collections
input = sys.stdin.readline

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

test_case = ri()

def solve():
    how to program like this?
    pass

for _ in range(test_case):
    
    print(solve())