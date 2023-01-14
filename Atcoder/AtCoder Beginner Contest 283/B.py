import math
mod = 10**9 + 7
N = int(input())
a = list(map(int, input().split()))


Q = int(input())
while Q:
	s = input()
	if s[0] == '1':
		_, k, x = map(int, s.split())
		a[k-1] = x
	elif s[0] == '2':
		_, k = map(int, s.split())
		print(a[k-1])
	Q -= 1
