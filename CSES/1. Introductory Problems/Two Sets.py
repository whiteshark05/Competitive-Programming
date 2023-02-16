import sys, math, itertools, functools, collections
input = sys.stdin.readline
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

n = ri()
a = [x for x in range(1,n +1)]
def solve():
	S = n*(n+1)//2
	if S % 2 == 1: return False, 0, [], 0, []
	target = S//2
	cur = 0 
	seen = collections.Counter()
	seen[0] = -1
	cur = 0
	[l, r] = [-1, -1]
	for i, num in enumerate(a):
		cur += num
		if cur - target in seen:
			[l, r] = [seen[cur-target], i]
			break
		seen[cur] = i
	#print(l,r, seen)
	s1 = a[:l+1] + a[r+1:]
	s2 = a[l+1:r+1]
	return True, len(s1), s1, len(s2), s2


x, y1 ,z1, y2, z2 = solve()
if x:
	print('YES')
	print(y1)
	print(*z1)
	print(y2)
	print(*z2)
else:
	print('NO')
"""
0,1,2,3,4,5,6
1,2,3,4,5,6,7,8
target = 18

"""


