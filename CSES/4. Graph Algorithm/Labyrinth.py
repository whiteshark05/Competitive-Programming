import sys, math, itertools, functools, collections
input = sys.stdin.readline
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))
import collections
def solve():
    def bfs(r,c):
        q = collections.deque()
        q.append((r,c,''))
        a[r][c] = '#'

        while q:
            r,c,path = q.popleft()
            #print(a, r, c, path)
            for dr, dc, direction in [(0,-1,'L'), (0,1,'R'),(-1,0,'U'), (1,0, 'D')]:
                row = r + dr
                col = c + dc
                new_path = path + direction
                if 0 <= row < n and 0 <= col < m and a[row][col] != '#':
                    if a[row][col] == 'B':
                        return new_path
                    elif a[row][col] == '.':
                        q.append((row,col,new_path))
                        a[row][col] = '#'
        return ''

    path = []
    for r in range(n):
        for c in range(m):
            if a[r][c] == 'A':
                path = bfs(r,c)
                break

    if not path:
        print("NO")
    else:
        print("\n".join(["YES", str(len(path)), path]))

    
    
n, m = rmi()
a = []
for r in range(n):
	a.append(list(input()))
solve()