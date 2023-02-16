import sys, math, itertools, functools, collections
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

t = ri()
def solve():
		p = 1
		for num in a:
			p *= num
		if a[0]**2 == p: return 1
		for i in range(1,n):
			a[i] *= a[i-1]
			if a[i]**2 == p:
				#print(i)
				return i + 1
		#print(a)
		return -1
for test_case in range(t):
	n = ri()
	a = ra()
	print(solve())
