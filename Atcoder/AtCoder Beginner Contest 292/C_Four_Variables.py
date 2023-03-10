import sys, math, itertools, functools, collections
input = sys.stdin.readline
from math import floor, sqrt
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



def solve(N):
    def divisors(n):
        divisors = []
        for d in range(1, int(n**0.5)+1):
            if n % d == 0:
                divisors.append(d)
                if d != n//d:
                    divisors.append(n//d)
        if int(n**0.5)**2 == n:
            divisors.remove(int(n**0.5))
        return divisors
    
    
    count = 0
    for B in range(1, N+1):
        for A in range(1, min(N//B, N)+1):
            divisors = [d for d in range(1, N-A*B+1) if (N-A*B)%d == 0]
            count += len(divisors)
    return count




for _ in range(test_case):
    N = ri()
    print(solve(N))