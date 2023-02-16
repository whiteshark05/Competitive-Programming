import sys, math, itertools, functools, collections, heapq
from sortedcontainers import SortedList
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))
"""
8 3
2 4 3 5 8 1 2 1

[2 4 3] 5 8 1 2 1
2 [4 3 5] 8 1 2 1
2 4 [3 5 8] 1 2 1
2 4 3 [5 8 1] 2 1

low = [2,3]
high = [4]
3 4 5 5 2 1
"""
n, k  = rmi()
A = ra()
ans = []
l = 0
window = SortedList()

def calMedian(arr):
	n = len(arr)
	if n % 2 == 0:
		return (arr[n//2] + arr[n//2-1])/2
	else:
		return arr[n//2]

for r in range(n - k + 1):
	if len(window) == k:
		ans.append(calMedian(window))
		window.remove(A[l])
		l += 1
	window.add(A[r])
	
print(*ans)

