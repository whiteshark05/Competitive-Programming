import math
N = int(input())
A = list(map(int, input().split()))
inf = 10**9 + 7

def solve(i):
	dp = [inf for _ in range(N)]
	dp[0] = 0
	for i in range(N):
		for j in range(i+1, i+3):
			if j < N:
				dp[j] = min(dp[j], dp[i] + abs(A[j] - A[i]))
	return dp[-1]
print(solve(N))