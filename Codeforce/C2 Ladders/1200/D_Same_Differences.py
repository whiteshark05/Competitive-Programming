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
    ans = 0
    count = collections.Counter()
    for i, num in enumerate(A):
        count[num - i] += 1
    
    for v in count.values():
        ans += v*(v-1)//2
    return ans
    pass

for _ in range(test_case):
    n = ri()
    A = ra()
    print(solve())