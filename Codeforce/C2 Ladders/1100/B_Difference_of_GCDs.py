import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

test_case = ri()

#-------- DIFFERENT WAYS TO UNSTUCK ------------ 
# 1. Frequency/Value domain and Pigeon Hole Principle 
# 2. Search from end to start instead of start to end
# 3. Prefix Suffix
# 4. Brute force if small input size

def solve(n, l, r):
    #if n > (r - l + 1): return False, None
    ans = []
    for i in range(n):
        num = int(math.ceil(l/(i+1))) * (i+1)
        if num <= r:
            ans.append(num)
        else:
            return False, None
    
    return True, ans
    pass

for _ in range(test_case):
    n, l , r = rmi()
    x, y = solve(n,l,r)
    if x:
        print('YES')
        print(*y)
    else:
        print('NO')