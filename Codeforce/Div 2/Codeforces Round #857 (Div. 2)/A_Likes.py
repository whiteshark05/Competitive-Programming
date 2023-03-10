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
    pos_ans = []
    neg_ans = []
    pos = 0
    neg = 0
    for num in A:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
    
    for i in range(1, pos+1):
        pos_ans.append(i)

    cur = pos_ans[-1] if pos_ans else 0
    
    for i in range(neg):
        cur -= 1
        pos_ans.append(cur)
    
    
    if pos > neg:
        tmp = pos - neg
        neg_ans = [1, 0] * neg + [x for x in range(1, tmp + 1)]
    else:
        tmp = neg - pos
        neg_ans = [1, 0] * neg + [0] * tmp

        


    return pos_ans, neg_ans
    pass

for _ in range(test_case):
    n = ri()
    A = ra()
    x, y = solve()
    print(*x)
    print(*y)