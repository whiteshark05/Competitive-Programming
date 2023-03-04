import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

test_case = 1

#-------- DIFFERENT WAYS TO UNSTUCK ------------ 
# 1. Frequency/Value domain and Pigeon Hole Principle 
# 2. Search from end to start instead of start to end
# 3. Prefix Suffix
# 4. Brute force if small input size

def solve():
    l = 0
    r = 10**18

    #dp = [[[-1 for _ in range(2)] for _ in range(200)] for _ in range(20)]

    @functools.lru_cache(None)
    #dp = {}
    def countPerfectNumber(index, digitSum, tight, nums):
        if index == len(nums):
            return digitSum == 10
        
        #key = (index, digitSum, tight, nums)
        #if key in dp:
            #return dp[key]
        
        res = 0
        k = int(nums[index]) if tight else 9

        for d in range(k+1):
            res += countPerfectNumber(index + 1, digitSum + d, tight & (d == k), nums)

        #if not tight:
            #dp[key] = res
        return res


    while l != r:
        m = (l + r) >> 1
        M = str(m)
        if countPerfectNumber(0,0,True,M) >= k:
            r = m
        else:
            l = m + 1
    return l

for _ in range(test_case):
    k = ri()
    print(solve())