import sys, math, itertools, functools, collections
input = sys.stdin.readline
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

n, x = rmi()
a = ra()
count = collections.Counter({0:1})
sum_so_far = 0
ans = 0
for num in a:
	sum_so_far += num
	if sum_so_far - x in count:
		ans += count[sum_so_far - x]
	count[sum_so_far] += 1
print(ans)