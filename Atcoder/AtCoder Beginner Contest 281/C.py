N, T = map(int, input().split())
A = list(map(int, input().split()))

cur_time = 0 
i = 0
total = sum(A)
T %= total
while cur_time + A[i] < T:
	cur_time += A[i]
	i = (i + 1) % N

print(i+1, T - cur_time)