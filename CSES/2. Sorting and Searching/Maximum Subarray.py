rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))
inf = 10**18
def solve():
    ans = -inf
    cur = -inf
    for num in a:
    	cur = max(cur + num, num)
    	ans = max(ans, cur)
    return ans

n = ri()
a = ra()
print(solve())
