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
    # Find the smallest gcd of any 2 different numbers
    # If it is less than or equal to 2, we can always make the prefix good by putting them as first and second elements
    for i in range(n-1):
        for j in range(i+1, n):
            if math.gcd(A[i],A[j]) <= 2:
                return True
    return False

for _ in range(test_case):
    n = ri()
    A = ra()
    print('Yes' if solve() else 'No')