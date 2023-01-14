n = int(input())
a = list(map(int, input().split()))
 
ans = 0
cur = a[0]
for num in a[1:]:
	if num < cur:
		ans += cur - num
	elif num == cur:
		continue
	else:
		cur = num
print(ans)