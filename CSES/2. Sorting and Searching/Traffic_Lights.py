import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

test_case = ri()

#-------- DIFFERENT WAYS TO UNSTUCK ------------ 
# 1. Frequency/Value domain and Pigeon Hole Principle 
# 2. Search from end to start instead of start to end
# 3. Prefix Suffix
# 4. Brute force if small input size

def solve():
    Intervals = [[0,x]]
    i = -1
    ans = []
    for num in A:
        for s, e in Intervals:
            if s <= num <= e:
                edit = i
                break
        
        Intervals[i][1] = num
        best = 0
        for s, e in Intervals:
            best = max(best, s - e)
        ans.append(best)

    return ans
    pass

for _ in range(test_case):
    x, n = rmi()
    A = ra()
    print(solve())