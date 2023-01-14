import math
inf = 10**9 + 7
N, W = map(int, input().split())
weights = [0] * N
values = [0] * N
for i in range(N):
	weights[i], values[i] = map(int, input().split())
V = sum(values)
dp = [[inf] * (V + 1) for i in range(N)] #Minimum amount of weights to get v value
dp[0][0] = 0

def solve():
	for i in range(N):
		for v in range(V + 1):
			if v >= values[i]:
				dp[i][v] = min(dp[i-1][v], dp[i-1][v - values[i]] + weights[i])
			else:
				dp[i][v] = min(dp[i-1][v], dp[i][v])
			

	ans = 0
	for i in range(V+1):
		if dp[-1][i] <= W:
			ans = max(ans, i)

	print(dp)
	return ans
	
print(solve())
