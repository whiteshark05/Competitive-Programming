t = int(input())
a= []

def solve(k,n):
    cur = 1
    dif = 0
    ans = []
    for _ in range(k):
        cur += dif  
        ans.append(cur)
        dif += 1

    return ans

for _ in range(t):
    k, n = list(map(int, input().split()))
    print(solve(k,n))