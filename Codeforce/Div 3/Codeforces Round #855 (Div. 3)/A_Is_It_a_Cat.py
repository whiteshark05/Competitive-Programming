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
def solve():
    S = s.lower()
    prev = ''
    ans = ''
    for c in S:
        if c != prev:
            ans += prev
            prev = c
    if prev:
        ans += prev
    #print(ans)
    
    return ans == 'meow'

for _ in range(test_case):
    n = ri()
    s = rs()
    print('YES' if solve() else 'NO')