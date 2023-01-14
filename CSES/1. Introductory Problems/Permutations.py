n = int(input())
 
if n == 2 or n == 3: 
	print("NO SOLUTION")
	exit(0)
ans = []
for i in range(2, n+1, 2):
	ans.append(str(i))
	
for i in range(1, n+1, 2):
	ans.append(str(i))
 
 
 
print(' '.join(ans))