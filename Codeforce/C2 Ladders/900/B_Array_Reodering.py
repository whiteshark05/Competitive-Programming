import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

test_case = ri()

def solve(A):
    A.sort(key = lambda x: (x % 2 == 1))
    #print(A)
    ans = 0
    for i, num1 in enumerate(A):
        for j in range(i+1, len(A)):
            if math.gcd(num1, 2*A[j]) > 1:
                ans += 1
    return ans


    pass

for _ in range(test_case):
    N = ri()
    A = ra()
    print(solve(A))