import math
mod = 10**9 + 7
N = int(input())
P = list(map(float, input().split()))

dp = [0] * (N + 1) 
dp[0]= 1

def solve():
	for coin in range(N):
		phead = P[coin]
		for head in range(coin + 1, -1, -1):
			dp[head] = (dp[head - 1] * phead if head > 0 else 0) + dp[head] * (1 - phead)
			
	
	ans = 0
	for head in range(N+1):
		if head > N - head:
			ans += dp[head]
	return ans			
print(solve())