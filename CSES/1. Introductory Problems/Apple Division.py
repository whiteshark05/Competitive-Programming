import sys, math, itertools, functools, collections
input = sys.stdin.readline
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))
inf = 10**18
n = ri()
a = ra()
S = sum(a)
threshold = (S + 2 - 1)//2
ans = [inf]
def dfs(i, cur_sum, path):
	#nonlocal ans
	if cur_sum >= threshold:
		ans[0] = min(ans[0], abs(S - cur_sum*2))
		return
	for j in range(i,n):
		dfs(j+1, cur_sum + a[j], path + [a[j]])
dfs(0, 0, [])
print(ans[0])
