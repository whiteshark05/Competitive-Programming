import sys, math, itertools, functools, collections
input = sys.stdin.readline
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

def solve():
	ans = 0
	seen = [False] * (n + 1)
	for i in range(n):
		if not seen[a[i]]:
			seen[a[i]] = True
			for j in range(i, n):
				if a[j] >= a[i] and not seen[a[j]]:
					seen[a[j]] = True
			ans += 1
	return ans
    
n = ri()
a = ra()
print(solve())