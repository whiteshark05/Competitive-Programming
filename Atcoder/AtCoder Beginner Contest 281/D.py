import itertools
N, K, D = map(int, input().split())
a = list(map(int, input().split()))

dp = [[[-1 for _ in range(D)] for i in range(K+1)] for j in range(N+1)]
dp[0][0][0] = 0
for i in range(N):
	for j in range(K+1):
		for k in range(D):
			if dp[i][j][k] == -1: continue

			#Transition when a[i] is not chosen
			dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])

			#Transition when a[i] is chosen
			if j != K:
				dp[i+1][j+1][(k + a[i])%D] = max(dp[i+1][j+1][(k+a[i])%D], dp[i][j][k] + a[i])

#print(dp)
print(dp[-1][-1][0])