t = int(input())
def solve(a,b):
	if (a == 0 and b > 0) or (b == 0 and a > 0) or (b > 2 * a) or (a > 2 * b): return False
	a %= 3
	b %= 3
	return (a,b) in [(0,0),(1,2),(2,1)]
 
for _ in range(t):
	a, b = map(int, input().split())
	print('YES' if solve(a,b) else 'NO')