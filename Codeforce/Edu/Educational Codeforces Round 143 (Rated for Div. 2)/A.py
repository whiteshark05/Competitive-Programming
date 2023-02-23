import sys, math, itertools, functools, collections
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

def solve():

	#print(tmp)
	#print(s.strip(), t.strip(), s + t)
	#tmp = s + t[::-1]
	i = 0
	j = len(tmp) - 1
	
	while i < len(tmp) - 1 and tmp[i] != tmp[i+1]:
		i += 1

	while j > 0 and tmp[j] != tmp[j-1]:
		j -= 1

	#print(tmp, i,j)
	return i + 1 >= j

t = ri()
for _ in range(t):
	n, m = rmi()
	s = input()
	t = input()
	tmp = ''.join((s + t[::-1]).split('\n'))
	print('YES' if solve() else 'NO')
