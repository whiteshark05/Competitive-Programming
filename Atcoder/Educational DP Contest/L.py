import math
mod = 10**9 + 7
N = int(input())
A = list(map(int, input().split()))

#dp is the score difference between Taro and Jiro
dp = [[0] * (N) for _ in range(N)]
# Taro moves first, when i == 0 and j == N - 1
def solve():
	for l in range(N - 1, -1, -1):
		for r in range(l, N):
			if l == r:
				dp[l][r] = A[l]
			else:
				dp[l][r] = max(A[l] - dp[l+1][r], A[r] - dp[l][r-1])
			
	return dp[0][-1]
print(solve())