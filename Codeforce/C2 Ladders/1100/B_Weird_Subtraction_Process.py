import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

test_case = 1

#-------- DIFFERENT WAYS TO UNSTUCK ------------ 
# 1. Frequency/Value domain and Pigeon Hole Principle 
# 2. Search from end to start instead of start to end
# 3. Prefix Suffix
# 4. Brute force if small input size

def solve(a,b):
    while True:
        if a == 0 or b == 0:
            return a, b
        elif a >= 2*b:
            a = a % (2*b)
        elif b >= 2*a:
            b = b % (2*a)
        else:
            break
    return a,b

for _ in range(test_case):
    a, b = rmi()
    print(*solve(a,b))