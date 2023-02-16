import collections, heapq, itertools, math, bisect
groupby = itertools.groupby
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

def solve():
	sub = []
	for x in a:
	    if len(sub) == 0 or sub[-1] < x:
	        sub.append(x)
	    else:
	        idx = bisect.bisect_left(sub, x)  # Find the index of the first element >= x
	        sub[idx] = x  # Replace that number with x
	return len(sub)
    
n = ri()
a = ra()
print(solve())