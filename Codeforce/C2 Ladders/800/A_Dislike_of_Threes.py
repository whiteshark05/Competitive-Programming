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
    count = 0
    ans = -1
    for num in range(1, 10000):
        ok1 = num % 3 == 0
        ok2 = num % 10 == 3

        if ok1: continue
        if ok2: continue
        #print(num)
        count += 1
        
        if count == n:
            ans = num
            break
    return ans



for _ in range(test_case):
    n = ri()
    print(solve())