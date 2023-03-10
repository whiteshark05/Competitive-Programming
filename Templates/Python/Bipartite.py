import sys, math, itertools, functools, collections
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))


n, m = rmi()
edges = []
adj = [[] for _ in range(n)]

for _ in range(m):
    u, v  = rmi()
    u -=  1
    v -= 1
    edges.append((u,v))
    adj[u].append(v)
    adj[v].append(u)

color = [-1]*n
ok = True

def dfs(u,c):
    color[u] = c + 1
    for v in adj[u]:
        if color[v] == -1:
            dfs(v, 1 - c)
        elif color[v] == color[u]:
            ok = False
            break

for i in range(n):
    if color[i] == -1:
        dfs(i, 0)

if not ok:
    print('IMPOSSIBLE')
    exit()
else:
    print(*color)



class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)
        
        for person, disliked in dislikes:
            adj[person].append(disliked)
            adj[disliked].append(person)
            
        
        colors = {}
        
        for person in range(1,n):
            if person not in colors:
                colors[person] = 0
                stack = [person]
                 
                while stack:
                    curr = stack.pop()
                    
                    for nei in adj[curr]:
                        if nei not in colors:
                            colors[nei] = colors[curr] ^ 1
                            stack.append(nei)
                            
                        elif colors[nei] == colors[curr]:
                            return False
        return True