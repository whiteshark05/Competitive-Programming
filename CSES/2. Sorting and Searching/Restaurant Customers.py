rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

tmp = []
def solve():
	tmp.sort()
	count = 0
	ans = 0
	for v, t in tmp:
		if t == 'start':
			count += 1
		else:
			count -= 1
		if count > ans:
			ans = count
	return ans
    
n = ri()
for _ in range(n):
	a, b = rmi()
	tmp.append([a,'start'])
	tmp.append([b, 'end'])

print(solve())