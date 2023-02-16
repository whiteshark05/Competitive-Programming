
t = int(input())

def solve(nums):
    a, b = nums[0]
    c, d = nums[1]
    MIN = min(a,b,c,d)
    MAX = max(a,b,c,d)
    return (a == MIN and d == MAX and a < b < d and a < c < d) or (b == MIN and c == MAX and b < a < c and b < d < c) or (c == MIN and b == MAX and c < a < b and c < d < b) or (d == MIN and a == MAX and d < c < a and d < b < a)

for _ in range(t):
    
    A = []
    for _ in range(2):
        A.append(map(int, input().split()))

    print('YES' if solve(A) else 'NO')