import sys, math, itertools, functools, collections
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

t = ri()
def solve():
	def sum_digit(n):
		ans = 0
		while n:
			ans += n%10
			n //= 10
		return ans

	for i in range(n+1):
		print(i, sum_digit(i), sum_digit(i) - sum_digit(n-i))
		#if abs(sum_digit(i) - sum_digit(n-i)) <= 1:
			#return [i, n-i]

for test_case in range(t):
	n = ri()
	print(*solve())