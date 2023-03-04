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
def solve(a,b):
    n, m = len(a), len(b)
    if n > m:
        a, b = b , a
    
    tmp = []
    ok = False
    ans = ''

    for i in range(len(a)-1):
        if b.find(a[i:i+2]) != -1:
            ok = True
            ans = '*'+a[i:i+2]+'*'
            return ok, ans

    if a[0] == b[0]:
        ok = True
        ans = a[0] + '*'
        return ok, ans
        
    elif a[-1] == b[-1]:
        ok = True
        ans = '*' + a[-1]
        return ok, ans

    return ok, ans
for _ in range(test_case):
    a = rs()
    b = rs()
    ok, ans = solve(a,b)
    if ok:
        print('YES')
        print(ans)
    else:
        print('NO')