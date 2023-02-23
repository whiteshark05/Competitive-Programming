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
    num = list(map(int,str(n)))
    tmp = 0
    for i in range(len(num)-2, -1, -1):
        if num[i] + num[i+1] >= 10:
            num[i+1] += num[i] - 10
            num[i] = 1
            break
        else:
            

    return ''.join(map(str, num))
    pass

for _ in range(test_case):
    n = ri()
    print(solve())