import sys, math, itertools, functools, collections
input = sys.stdin.readline
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

n, k = rmi()
a = ra()
"""
5 3
2 4 7  3  5
S = 21
k = 3
threshold = 7

"""
#a = list(accumulate(a))
S = sum(a)
l = max(a)
r = S
ans = 0 
def ok(m):
	have  = 0
	cur = 0
	for num in a:
		if cur + num > m:
			have += 1
			cur = 0
		cur += num
		
	if cur > 0:
		have += 1	 
	return have <= k

while l != r:
	m = (l + r) >> 1
	if ok(m):
		r = m
	else:
		l = m + 1
print(l)