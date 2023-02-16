import sys, math, itertools, functools, collections
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

N = ri()
for n in range(1,N+1):
	ans = n**2*(n**2-1)//2 - 4*(n-1)*(n-2)
	print(ans)