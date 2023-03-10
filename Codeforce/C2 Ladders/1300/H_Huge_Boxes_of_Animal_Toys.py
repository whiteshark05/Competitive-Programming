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
    ans = ['Tidak' for _ in range(4)]
    if (A + B) % 2 == 1:
        if B + C > 0:
            ans[1] = 'Ya'
        if A + D > 0:
            ans[0] = 'Ya'
    else:
        if B + C > 0:
            ans[2] = 'Ya'
        if A + D > 0: 
            ans[3] = 'Ya'
    return ans
    

for _ in range(test_case):
    A, B, C, D = rmi()
    print(*solve())