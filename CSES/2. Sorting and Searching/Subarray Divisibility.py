import sys, math, itertools, functools, collections
input = sys.stdin.readline
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

n = ri()
a = ra()
ans = 0
count = collections.Counter({0:1})
sum_so_far = 0
for num in a:
	sum_so_far += num
	sum_so_far %= n
	if sum_so_far in count:
		ans += count[sum_so_far]
	count[sum_so_far] += 1
print(ans)