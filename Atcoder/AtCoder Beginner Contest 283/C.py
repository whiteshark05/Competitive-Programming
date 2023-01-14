s = input()
n = len(s)
ans = 0
l = 0
for i in range(n):
	if s[i] != '0':
		ans += l // 2 + l % 2
		ans += 1
		l = 0	
	else:
		l += 1
if l:
	ans += l // 2 + l % 2
print(ans)