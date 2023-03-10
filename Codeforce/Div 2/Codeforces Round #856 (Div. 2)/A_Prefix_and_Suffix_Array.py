import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
ras = lambda: [x for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

test_case = ri()

#-------- DIFFERENT WAYS TO UNSTUCK ------------ 
# 1. Frequency/Value domain and Pigeon Hole Principle 
# 2. Search from end to start instead of start to end
# 3. Prefix Suffix
# 4. Brute force if small input size

def solve():
    tmp = []
    for s in A:
        if len(s) == n - 1:
            tmp.append(s)
    a, b = tmp[0], tmp[1]
    if a[1:] == b[:-1]:
        c = a + b[-1]
    else:
        c = b + a[-1]
    #print(c)
    return c == c[::-1]
    
    pass

for _ in range(test_case):
    n = ri()
    A = ras()
    print('YES' if solve() else 'NO')




import sys, math, itertools, functools, collections
input = sys.stdin.readline

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

test_case = ri()

def solve():
    
    pass

for _ in range(test_case):
    
    print(solve())