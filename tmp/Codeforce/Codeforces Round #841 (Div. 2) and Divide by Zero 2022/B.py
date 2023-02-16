t = int(input())
mod = 10**9 + 7

def solve(n):
	ans = 2 * n - 1
	return (2022 * ans) % mod

for _ in range(t):
	n = int(input())
	print(solve(n))