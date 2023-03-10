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
def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    while(True):
        if((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

def solve():
    L = A + [1]
    B = [1] * len(L)
    for i in range(1, len(L)):
        B.append(lcm(L[i],L[i-1]))
    
    for i in range(1,len(B)):
        if math.gcd(B[i],B[i+1]) != A[i]:
            return False
    return True

for _ in range(test_case):
    n = ri()
    A = ra()
    print('YES' if solve() else 'NO')