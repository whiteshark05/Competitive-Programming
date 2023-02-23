import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

test_case = ri()

def solve(x,y):
    if x < y:
        x, y = y, x
    ans = x - y
    if ans == 0: return [0,0]
    return [ans, min(ans - (y % ans), y % ans)]
    
    pass

for _ in range(test_case):
    x, y = rmi()
    #print(x,y)
    print(*solve(x,y))