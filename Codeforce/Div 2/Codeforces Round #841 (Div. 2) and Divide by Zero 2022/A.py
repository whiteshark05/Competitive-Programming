t = int(input())

def solve(n, a):
	p = 1
	for num in a:
		p*=num
	return 2022 * ((n - 1) + p)

for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	print(solve(n,a))



