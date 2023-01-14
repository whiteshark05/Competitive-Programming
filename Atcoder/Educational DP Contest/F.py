import math
inf = 10**9 + 7
s1 = input()
s2 = input()

M = len(s1)
N = len(s2)
dp = [[0] * (N + 1) for i in range(M + 1)]

def solve():
	for i in range(1, M + 1):
		for j in range(1, N + 1):
			if s1[i-1] == s2[j-1]:
				dp[i][j] = dp[i-1][j-1] + 1 
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])

	i = M 
	j = N 
	ans = ''
	
	while i > 0 and j > 0:
		if s1[i-1] == s2[j-1]:
			ans = s1[i-1] + ans
			i -= 1 
			j -= 1
		elif dp[i][j-1] > dp[i-1][j]:
			j -= 1
		else:
			i -= 1
				
	return ans
print(solve())
