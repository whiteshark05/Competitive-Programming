import sys, math, itertools, functools, collections
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

n = ri()
a = ra()
stack = []
ans = [0]*n
for i in range(n-1, -1, -1):
	while stack and a[stack[-1]] > a[i]:
		ans[stack.pop()] = i + 1
	stack.append(i)
print(*ans)