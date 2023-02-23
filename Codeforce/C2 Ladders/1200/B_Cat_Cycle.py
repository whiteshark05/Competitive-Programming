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
    step = k - 1
    if n % 2 == 0:
        return 1 + step % n
    else:
        cycle_length = n // 2
        cycle_no, rem = divmod(step, cycle_length)
        return 1 + (step + cycle_no) % n 

    pass

for _ in range(test_case):
    n, k = rmi()
    print(solve())