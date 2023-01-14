import math
inf = 10**9 + 7
N, W = map(int, input().split())
weights = [0] * N
values = [0] * N
for i in range(N):
	weights[i], values[i] = map(int, input().split())
dp = [[0] * (W + 1) for i in range(N)]

def solve():
	for i in range(N):
		for w in range(W + 1):
			if weights[i] > w:
				dp[i][w] = dp[i-1][w]
			else:
				dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i]] + values[i])
			
	print(dp)			
	return dp[-1][-1]
print(solve())

