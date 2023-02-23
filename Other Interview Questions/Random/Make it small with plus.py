"""
You want to create a formula by inserting a plus sign between strings of only numbers. At this time, the formula

We are trying to find a way to make the scatter value the smallest.

For example, given the string 1234567 and you can insert a plus sign up to 2 times into it,

Valid expressions include 1+2+34567 , 12+34+567 , 12+3+4567 , ... Among these, the final value

The way to make a minimum sum is 123+45+67. In this case, the result of the formula is 235.



A string of non-zero numbers, num , and an integer representing the number of times a plus sign can be inserted.

k is given as a parameter. When creating a formula by inserting a plus sign, the most

Please complete the solution function to return a small value. However, since the result value can be very large, 10^9

+ Return the remainder after dividing by 7.



Constraints:

2 <= num.length <= 1000
num is consists of 1~9

(num.length / 10)<= k < = (num.length - 1)
Example of input and output.





num (input)	k (input)	Result (output)
"1234567"	2	235
"555555"	2	165
"91911919"	3	166
"""
import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

inf = 10**18
test_case = 1

def solve():
    
    N = len(S)
    #@functools.lru_cache(None)
    def dp(i, k):
        if i == N:
            return inf
        
        if k == 0:
            return inf

        best = inf
        for j in range(i+1, N):
            best = min(best, dp(j+1, k-1) + int(S[:j]))
        return best
    return dp(0, K) % 7

    

for _ in range(test_case):
    S = rs()
    K = ri()
    print(solve())