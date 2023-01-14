import collections, heapq, itertools, math
groupby = itertools.groupby
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))
mod = 10**9+7
inf = 10**10
def getOptions(n):
	seen = {0}
	while n:
		if n%10 not in seen:
			seen.add(n%10)
		n//=10
	return list(seen)

def solve():
    dp = [0] + [inf] * (n) 
    for i in range(n):
    	for num in getOptions(i):
    		if i + num <= n - 1:
    			dp[i+num] = min(dp[i+num], dp[i] + 1)

    print(dp)
    return dp[-1]

    
n = ri()
print(solve())