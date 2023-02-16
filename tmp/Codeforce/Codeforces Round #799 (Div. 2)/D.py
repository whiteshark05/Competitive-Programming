t = int(input())
a= []
ans = []
def solve(s, x):
    hh, mm = s.split(':')
    return hh, mm


for _ in range(t):
    nums = list(map(int, input().split()))
    ans.append(solve(s, x))

for a in ans:
    print(a)