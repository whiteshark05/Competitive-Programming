import math
mod = 10**9 + 7
H, W = map(int, input().split())
A = []
for r in range(H):
	A.append(list(input()))

dp = [[0] * W for i in range(H)]
dp[0][0] = 1

def solve():
	for r in range(H):
		for c in range(W):
			if c + 1 < W  and A[r][c+1] != '#':
				dp[r][c+1] += dp[r][c]

			if r + 1 < H and A[r+1][c] != '#':
				dp[r+1][c] += dp[r][c]

	#print(dp)
	return dp[-1][-1] % mod
print(solve())
