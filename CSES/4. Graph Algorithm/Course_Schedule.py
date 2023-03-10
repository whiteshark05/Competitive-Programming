import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

test_case = 1

#-------- DIFFERENT WAYS TO UNSTUCK ------------ 
# 1. Frequency/Value domain and Pigeon Hole Principle 
# 2. Search from end to start instead of start to end
# 3. Prefix Suffix
# 4. Brute force if small input size

def solve():
    adj = [[] for _ in range(n)]
    indegree = [0] * n
    for _ in range(m):
        u, v = rmi()
        u -= 1
        v -= 1
        adj[u].append(v)
        indegree[v] += 1

    stack = []
    ans = []

    #print(adj)
    count = 0
    for i in range(n):
        if indegree[i] == 0:
            stack.append(i)

    while stack:
        u = stack.pop()
        ans.append(u+1)
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                stack.append(v)
                

    if len(ans) == n:
        return True, ans
    else:
        return False, None

for _ in range(test_case):
    n, m = rmi()
    x,y = solve()
    if x:
        print(*y)
    else:
        print("IMPOSSIBLE")