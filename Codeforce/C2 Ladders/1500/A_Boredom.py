import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

test_case = 1

def solve():
    freq = [0] * (10**5 + 1)
    for num in A:
        freq[num] += num

    skip, take = 0, 0
    
    for i in range(1, 10**5 + 1):
        take, skip = max(take, skip + freq[i]), take
        
    return max(skip, take)


for _ in range(test_case):
    n = ri() 
    A = ra()
    print(solve())