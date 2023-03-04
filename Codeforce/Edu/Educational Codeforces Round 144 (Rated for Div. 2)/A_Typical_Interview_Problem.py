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
    tmp = ''
    for i in range(1, 10*5):
        if i % 3 == 0 and i % 5 == 0:
            tmp += 'FB'
        elif i % 3 == 0:
            tmp += 'F'
        elif i % 5 == 0:
            tmp += 'B'
    
    index = tmp.find(s)
    return index != -1

for _ in range(test_case):
    k = ri()
    s = rs()
    print('YES' if solve() else 'NO')