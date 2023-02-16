n = int(input())
a = list(map(int, input().split()))
 
ans = 0
for i, num in enumerate(a):
	ans ^= (i + 1)
	ans ^= num
print(ans^n)