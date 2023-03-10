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
    total = 0
    for num in A:
        if num == 1:
            total += 1
    
    j = len(A) - 1
    count = 0
    ans = 0
    while j >= 0:
        if A[j] == 1:
            count += 1     
        else:
            countLeft = total - count
            if countLeft > 1:
                countLeft = 1 + math.ceil((countLeft-1)/2) 
            ans = max(ans, count + countLeft)
            total -= count
            count = 0
        j -= 1
    
    if count:
        ans = max(ans, count)
    return ans
    

for _ in range(test_case):
    n = ri()
    A = ra()
    print(solve())