import sys, math, itertools, functools, collections
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

N = ri()
A = ra()
M = ri()
B = ra()
X = ri()

dp = [0] * (X + 1)
for trap in B:
	dp[trap] = -1
dp[0] = 1


for i in range(X+1):
	for step in A:
		if i + step <= X and dp[i] == 1 and dp[i+step] != -1:
			dp[i+step] = 1
#print(dp)
print('Yes' if dp[-1] == 1 else 'No')
