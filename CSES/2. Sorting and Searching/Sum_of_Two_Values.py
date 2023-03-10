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
	m = {}
	for i, num in enumerate(a):
		if x - num in m:
			return [m[x-num] + 1, i + 1]
		m[num] = i
	return [-1, -1]    
 
n, x = rmi()
a = ra()    
if solve() != [-1, -1]:
	pa(solve())
else:
	print("IMPOSSIBLE") 