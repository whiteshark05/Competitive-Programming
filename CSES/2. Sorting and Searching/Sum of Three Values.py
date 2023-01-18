import collections, heapq, itertools, math
groupby = itertools.groupby
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))
 
def solve():
    ans = set()
    for i in range(n):
        if i > 0 and a[i-1] == a[i]: continue
        target = x - a[i]
        m = {}
        for j in range(i+1,n):
            if target - a[j] in m:
                ans.add(tuple(sorted([i + 1, j + 1, m[target - a[j]] + 1])))
            m[a[j]] = j
    return list(ans)
    
n, x = rmi()
a = ra()
ans = solve()
if len(ans) == 0:
    print('IMPOSSIBLE')
else:
    tmp = list(ans[0])
    pa(tmp)