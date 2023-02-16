import sys, math, itertools, functools, collections
input = sys.stdin.readline
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

for i in range(20):
	print(i, math.factorial(i))