import collections, heapq, itertools, math
groupby = itertools.groupby
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

def solve():
    for i in range(n-1):
    	if s[i] == 'L' and s[i+1] == 'R':
    		return 0
    	if s[i] == 'R' and s[i+1] == 'L':
    		return i + 1
    return -1
    
for t in range(ri()):
    n = ri()
    s = rs()
    print(solve())