import collections, heapq, itertools, math
groupby = itertools.groupby
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))
 
def solve():
    ans = 0
    a.sort()
    b.sort()
    i = n - 1
    j = m - 1
    while i >= 0 and j >= 0:
        if a[i] - k <= b[j] <= a[i] + k:
            i -= 1
            j -= 1
            ans += 1
        elif a[i] + k < b[j]:
            j -= 1
        else:
            i -= 1
 
    return ans
    
 
n, m, k = rmi()
a = ra()
b = ra()
print(solve())