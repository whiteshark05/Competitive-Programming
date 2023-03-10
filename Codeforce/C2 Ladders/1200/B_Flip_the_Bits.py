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
    a = s1+'0'
    b = s2+'0'
    count = 0
    for i in range(n):
        count += (a[i] == '1') - (a[i] == '0')
        if (a[i] == b[i]) != (a[i+1] == b[i+1]) and count != 0:
            return False
    return True
    pass

for _ in range(test_case):
    n = ri()
    s1 = rs()
    s2 = rs()
    print('YES' if solve() else 'NO')