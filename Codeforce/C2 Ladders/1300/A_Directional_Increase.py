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
    
    if sum(A) != 0:
        return False
    
    while A and A[-1] == 0:
        A.pop()

    pref = [0]
    for num in A:
        pref.append(pref[-1] + num)

    for i in range(1, len(pref)-1):
        if pref[i] <= 0:
            return False
    return True

for _ in range(test_case):
    n = ri()
    A = ra()
    print('Yes' if solve() else 'No')