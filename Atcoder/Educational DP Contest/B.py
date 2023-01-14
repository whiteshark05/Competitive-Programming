import math
N, K = map(int, input().split())
A = list(map(int, input().split()))
inf = 10**9 + 7

def solve(i, K):
	dp = [inf for i in range(N)]
	dp[0] = 0
	for i in range(N):
		for j in range(i + 1, i + K + 1):
			if j < N:
				dp[j] = min(dp[j], dp[i] + abs(A[j] - A[i]))
	return dp[-1]
print(solve(N, K))