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
    flipper = 0
    last_seen = -1
    for i in range(m):
        if A[0][i] == 'B' and A[1][i] == 'B':
            flipper ^= 1
        elif A[0][i] == 'B' and A[1][i] == 'W':
            if last_seen == 1 and flipper == 0:
                return False
            if last_seen == 0 and flipper == 1:
                return False
            last_seen = 0
            flipper = 0
        else:
            if last_seen == 1 and flipper == 1:
                return False
            if last_seen == 0 and flipper == 0:
                return False
            last_seen = 1
            flipper = 0
    return True


for _ in range(test_case):
    m = ri()
    A = []
    for _ in range(2):
        A.append(rs())
    print('YES' if solve() else 'NO')