t = int(input())
a= []
ans = []
def solve(n, nums):
    x = len(set(nums))
    if n%2 == x%2:
        return x
    else:
        return x - 1

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    ans.append(solve(n, nums))

for a in ans:
    print(a)