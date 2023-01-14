import collections, heapq, itertools, math
groupby = itertools.groupby
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

ans = [0] * n
def solve():
    c = collections.Counter(a)
    for v in c.values():
    	if n - v < v - 1: return False 

    k, v = c.most_common()[0]
    for i in range(n):
    	if i%2 == 0:
    		ans[i] = k
    	else:
    		
    return True
    
for t in range(ri()):
    n = ri()
    a = ra()
    if solve():
    	print('YES')
    	pa(ans)
    else:
    	print('NO')