rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

def solve():
    n = len(a)
    a.sort()
    ans = 0
    median = a[n//2]
    for num in a:
        ans += abs(median - num)
    return ans
    
n = ri()
a = ra()

print(solve())