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
    pattern = ['1','0','1']
    for r in range(R):
        for c in range(C):
            x1 = A[r-1][c-1] if r > 0 and c > 0 else '-1'
            x2 = A[r-1][c] if r > 0 else '-1'
            x3 = A[r-1][c+1] if r > 0 and c + 1 < C else '-1'
            y1 = A[r][c-1] if c > 0 else '-1'
            y2 = A[r][c]
            y3 = A[r][c+1] if c + 1 < C else '-1'
            z1 = A[r+1][c-1] if r + 1 < R and c > 0 else '-1'
            z2 = A[r+1][c] if r + 1 < R else '-1'
            z3 = A[r+1][c+1] if r + 1 < R and c + 1 < C else '-1'
            if y2 == '1' and ([y1,x1,x2] == pattern or [x2,x3,y3] == pattern or [y3,z3,z2] == pattern or [z2,z1,y1] == pattern):
                return False
            
    return True
    

for _ in range(test_case):
    R, C = rmi()
    A = []
    for _ in range(R):
        s = rs()
        A.append(s)
    

    print('YES' if solve() else 'NO')