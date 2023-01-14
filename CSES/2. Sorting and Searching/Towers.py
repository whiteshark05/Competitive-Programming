import collections, heapq, itertools, math, bisect
groupby = itertools.groupby
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))
 
def solve():
	stack = []
	for num in a:
		if not stack:
			stack.append(num)
		else:
			index = bisect.bisect_right(stack, num)
			if num >= stack[-1]:
				stack.append(num)
			else:
				stack[index] = num
 
	return len(stack)
    
 
n = ri()
a = ra()
print(solve())