import collections, heapq, itertools, math
groupby = itertools.groupby
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))
mod = 10**9+7
def solve():
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 4
    if n == 4: return 8
    if n == 5: return 16
    if n == 6: return 32
    f = [0]*(n+1)
    f[1] = 1
    f[2] = 2 
    f[3] = 4 
    f[4] = 8
    f[5] = 16
    f[6] = 32
    for i in range(7, n+1):
    	for j in range(1, 7):
    		f[i] += (f[i-j] % mod)
    return f[-1] % mod
    
n = ri()
print(solve())