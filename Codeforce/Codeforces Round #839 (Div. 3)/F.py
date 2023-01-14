t = int(input())
a= []

def solve(nums):
    return sum([nums[i] > nums[0] for i in range(len(nums))])

for _ in range(t):
    tmp = list(map(int, input().split()))
    print(solve(tmp))