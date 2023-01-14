import collections, heapq, itertools, math
groupby = itertools.groupby
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

def solve():
	#dp[i][j] longest subsequence ending at i
    dp = [1] * n
    dp[0] = 1
    for i in range(1,n):
    	for j in range(i):
    		if a[i] > a[j]:
    			dp[i] = max(dp[i], 1 + dp[j]) 
    return max(dp)
    
n = ri()
a = ra()
print(solve())