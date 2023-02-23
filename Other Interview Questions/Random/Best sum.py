"""
Best sum
We want to represent a natural number n greater or equal to 2 as the sum of two or more natural numbers. Each term of the ways to make n We'll call the method with the greatest product the "best sum."

For example n = 8,



1+1+1+1+1+1+1+1

1+2+2+3

2+2+2+2

3+3+2

4+4

There are several ways, but the best sum for 3 + 3 + 2 is 3 x 3 x 2 = 18. When a natural number n is given as a parameter, the solution is to return the value multiplied by the numbers that form the best sum Please complete the function.

Constraints:

n is a natural number greater than or equal to 2 and less than or equal to 100.

For input n, the product of the best summing numbers is a natural number less than or equal to 2 ^ 63 - 1.



Example of input and output



n	result
8	18
5	6
#1. 3 x 3 x 2 = 18 (3+3+2 makes 8)

#2. 3 x 2 = 6 (3+2 makes 5)
"""
import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
#ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

#test_case = 1

def solve(N):
    q, r = divmod(N, 3)
    if r == 0:
        return 3**q
    # r == 1 meaning q + r == 4. We break into (2,2) instead of (3,1)
    elif r == 1:
        return 3**(q-1)*4
    else:
        return 3**q*r
    
N = int(input())
print(solve(N))
#for _ in range(test_case):
