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
    if b == 1:
        return []
    ans = [a, a*b, a*(b+1)]
    return ans

for _ in range(test_case):
    a, b = rmi()
    ans = solve()
    if not ans:
        print('NO')
    else:
        print('YES')
        print(*ans)
