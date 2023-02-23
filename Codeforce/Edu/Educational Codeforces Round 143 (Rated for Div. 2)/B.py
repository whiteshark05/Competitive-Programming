import sys, math, itertools, functools, collections
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

for _ in range(ri()):
	n, k = rmi()
	tmp = [0] * 1000
	edges = []
	for _ in range(n):
		l, r = rmi()
		tmp[l] += 1
		tmp[r+1] -= 1
		edges.append([l,r])

	for i in range(1, len(tmp)):
		tmp[i] += tmp[i-1]

	#print(tmp)
	#interesting = []

	for i in range(len(tmp)):
		if i == k: continue
		if tmp[i] >= tmp[k]:
			#count = shared edges between i and k, cannot be removed, must be less than tmp[k]
			count = 0
			for l, r in edges:
				if l <= i <= r and l <= k <= r:
					count += 1
			if count >= tmp[k]:
				print('NO')
				break
	else:
		print('YES')




