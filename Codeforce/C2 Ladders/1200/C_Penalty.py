import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

test_case = ri()

def solve():
    cq1 = 0
    cq2 = 0
    g1 = 0
    g2 = 0
    left1 = 5
    left2 = 5
    for i, c in enumerate(s):
        if i % 2 == 0:
            if c == '?':
                cq1 += 1
            elif c == '1':
                g1 += 1
            
            left1 -= 1

            
        else:
            if c == '?':
                cq2 += 1
            elif c == '1':
                g2 += 1

            left2 -= 1

        if g1 + cq1 > g2 + left2 or g2 + cq2 > g1 + left1:
            return i + 1 
        
    return 10

    pass

for _ in range(test_case):
    s = rs()
    print(solve())