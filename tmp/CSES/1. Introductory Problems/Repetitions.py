s = input()
prev = ''
cur, ans = 0, 0
for c in s:
	if c == prev:
		cur += 1
		ans = max(ans, cur)
	else:
		cur = 1
		prev = c
if cur:
	ans = max(ans, cur)
print(ans)