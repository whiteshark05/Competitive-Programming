rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))
import collections
def solve():
    ans = 0

    def bfs(r,c):
    	q = collections.deque()
    	q.append((r,c))
    	a[r][c] = '#'

    	while q:
    		r,c = q.popleft()
    		for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
    			row = r + dr
    			col = c + dc
    			if 0 <= row < n and 0 <= col < m and a[row][col] == '.':
    				q.append((row,col))
    				a[row][col] = '#'

    for r in range(n):
    	for c in range(m):
    		if a[r][c] == '.':
    			ans += 1
    			bfs(r,c)
    return ans
    
n, m = rmi()
a = []
for r in range(n):
	a.append(list(input()))
#print(a)
print(solve())