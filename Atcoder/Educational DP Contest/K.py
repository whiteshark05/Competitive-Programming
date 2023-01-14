import math
mod = 10**9 + 7
N = int(input())
coins = list(map(float, input().split()))

dp = [0] * (N + 1)
dp[0] = 1
print(coins)
def solve():
	for p_head in coins:
		for i in range(N + 1):
			dp[i] = dp[i-1] * p_head if i > 0 else 0 + dp[i] * (1 - p_head) 
	print(dp)			
	return sum(dp[N//2:])
print(solve())