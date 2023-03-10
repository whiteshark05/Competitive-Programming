import sys, math, itertools, functools, collections, heapq
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))
inf = 10**18
test_case = 1

#-------- DIFFERENT WAYS TO UNSTUCK ------------ 
# 1. Frequency/Value domain and Pigeon Hole Principle 
# 2. Search from end to start instead of start to end
# 3. Prefix Suffix
# 4. Brute force if small input size

def solve():
    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]
    indegree = [0] * n
    dist = [-inf] * n
    p = [-1] * n
    dist[0] = 0
    stack = []
    for _ in range(m):
        u, v = rmi()
        u -= 1
        v -= 1
        adj[u].append(v)
        radj[v].append(u)
        indegree[v] += 1

    q = collections.deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)
    
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        #print(u, topo)
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    
    #print(topo)
    for cur in topo:
        for prev in radj[cur]:
            if cur > 0 and dist[cur] < dist[prev] + 1:
                dist[cur] = dist[prev] + 1
                p[cur] = prev
    
    #print(p, dist)
    temp = n - 1
    contains0 = False
    if temp == 0: contains0 = True

    while temp != -1 and dist[temp] >= 0:
        stack.append(temp)
        temp = p[temp]
        if temp == 0: contains0 = True
    ans = [x+1 for x in stack[::-1]]
    if contains0:
        print(len(ans))
        print(*ans)
    else:
        print("IMPOSSIBLE")
        
        

for _ in range(test_case):
    n, m = rmi()
    solve()