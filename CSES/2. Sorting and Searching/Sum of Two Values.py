rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

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
