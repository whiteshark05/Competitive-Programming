import collections, heapq, itertools, math
groupby = itertools.groupby
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

def ok(mid):
	return (mid + 1) * math.factorial(mid-1) % n == 0

def solve():
    l = 1
    r = n - 1

    while l != r:
    	mid = (l + r + 1) >> 1
    	if ok(mid):
    		l = mid
    	else:
    		r = mid - 1

    return l 
    
for t in range(ri()):
    n = ri()

    print(solve())