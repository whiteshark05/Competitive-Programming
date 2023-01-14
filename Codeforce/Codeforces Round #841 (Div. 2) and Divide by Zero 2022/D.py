t = int(input())

def solve(m, n, grid):
	def ok(mid):
		length = 0
		dp = [[0] * m for _ in range(n)]
		for r in range(n):
			for c in range(m):
				if grid[r][c] >= mid:
					dp[r][c] = 1
				else:
					dp[r][c] = 0
		
		for r in range(n):
			for c in range(m):
				if dp[r][c] == 1:
					dp[r][c] = 1 + min(dp[r-1][c-1] if r > 0 and c > 0 else 0, dp[r-1][c] if r > 0 else 0, dp[r][c-1] if c > 0  else 0)
				length = max(length, dp[r][c])

		return length >= mid

	l = 0
	r = min(m,n)
	while l != r:
		mid = (l + r + 1) >> 1
		if ok(mid):
			l = mid
		else:
			r = mid - 1
	return l

for _ in range(t):
	n, m = map(int, input().split())
	a = []
	for _ in range(n):
		a.append(list(map(int, input().split())))
	print(solve(m,n,a))



