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
    pos, neg, zero = [], [], []
    for i in range(n):
        if A[i] > 0 :
            pos.append(A[i])
        elif A[i] == 0:
            if len(zero) < 2:
                zero.append(A[i])
        elif A[i] < 0:
            neg.append(A[i])

    if len(pos) > 2 or len(neg) > 2:
        return False
    
    for num in pos:
        zero.append(num)

    for num in neg:
        zero.append(num)
    
    s = set(zero)
    for i in range(len(zero) - 2):
        for j in range(i+1, len(zero) - 1):
            for k in range(j+1, len(zero)):
                if zero[i] + zero[j] + zero[k] not in s:
                    return False
    return True




for _ in range(test_case):
    n = ri()
    A = ra()
    print('YES' if solve() else 'NO')