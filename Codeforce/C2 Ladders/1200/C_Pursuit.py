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
def ok(A,B,m):
    #S, T = [], 
    S = A + [100]*m
    T = B + [0]*m
    k = n + m
    S.sort()
    T.sort()
    have = sum(S) - sum(S[:k//4])
    need = sum(T) - sum(T[:k//4])
    #print(m, have, need)
    return have >= need

def solve():
    l = 0
    r = 10**5

    while l != r:
        m = (l + r) >> 1 
        if ok(A,B,m):
            r = m
        else:
            l = m + 1

    return l
    pass

for _ in range(test_case):
    n = ri()
    A = ra()
    B = ra()
    print(solve())