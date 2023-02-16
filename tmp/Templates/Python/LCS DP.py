#https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326308/C%2B%2BPython-DP-Binary-Search-BIT-Segment-Tree-Solutions-Picture-explain-O(NlogN)
#Is Subsequence
"""
Go through string 1, increment i if character match
if i reach the end then return true
"""
def isSubsequence(self, s: str, t: str) -> bool:
    i = 0
    for c in t:
        if i < len(s) and s[i] == c:
            i += 1
    return i == len(s)


#Longest common subsequence
a = [1, 2, 3, 4]
b = [2, 3, 4, 5 ,3]


def LCS(a, b):
	m = len(a)
	n = len(b)
	dp = [[0]*(n+1) for _ in range(m+1)]
	for i in range(1,m+1):
		for j in range(1, n+1):
			if a[i-1] == b[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
	return dp[-1][-1]
print(LCS(a,b))


#Longest palindromic subsequence
def longestPalindromeSubseq(self, s: str) -> int:
        # dp[i][j] = Longest PS between i:j
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        #print(dp)
        return dp[0][-1]

#Number of common subsequence
def NCS(a,b):
	m = len(a)
	n = len(b)
	dp = [[0]*(n+1) for _ in range(m+1)]
	for i in range(1,m+1):
		for j in range(1, n+1):
			if a[i-1] == b[j-1]:
				dp[i][j] = dp[i-1][j] + dp[i][j-1] + 1
			else:
				dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
	return dp[-1][-1]
s = "ajblqcpdz"
t = "aefcnbtdi"
print(NCS(s,t))



#Longest increasing subsequence
def lengthOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 0: return 0
    dp = [1 for n in range(n)]
    dp[0] = 1
    ans = 0
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp) 

class Solution:
    def pathOfLIS(self, nums: List[int]):
        sub = []
        subIndex = []  # Store index instead of value for tracing path purpose
        trace = [-1] * len(nums)  # trace[i] point to the index of previous number in LIS
        for i, x in enumerate(nums):
            if len(sub) == 0 or sub[-1] < x:
                if subIndex:
                    trace[i] = subIndex[-1]
                sub.append(x)
                subIndex.append(i)
            else:
                idx = bisect_left(sub, x)  # Find the index of the smallest number >= x, replace that number with x
                if idx > 0:
                    trace[i] = subIndex[idx - 1]
                sub[idx] = x
                subIndex[idx] = i

        path = []
        t = subIndex[-1]
        while t >= 0:
            path.append(nums[t])
            t = trace[t]
        return path[::-1]

print(Solution().pathOfLIS([2, 6, 8, 3, 4, 5, 1]))  # [2, 3, 4, 5]
#Longest common substring
#def LCSS(s1, s2):




