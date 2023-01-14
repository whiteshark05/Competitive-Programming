import math
inf = 10**9 + 7
N = int(input())
A = [0] * (N + 1) 
B = [0] * (N + 1) 
C = [0] * (N + 1)
for i in range(N):
	A[i], B[i], C[i] = map(int, input().split())
dp = [[0]*3 for i in range(N + 1)]
def solve():
	for i in range(1, N+1):
		dp[i][0] = max(dp[i-1][1] + B[i-1], dp[i-1][2] + C[i-1])
		dp[i][1] = max(dp[i-1][0] + A[i-1], dp[i-1][2] + C[i-1])
		dp[i][2] = max(dp[i-1][0] + A[i-1], dp[i-1][1] + B[i-1])
	return max(dp[-1])
print(solve())