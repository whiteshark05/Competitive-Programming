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
    count = [0] * m
    for num in A:
        count[num % m]+=1
    
    ans = 0
    #print(count)
    ans += count[0] != 0
    if m % 2 == 0:
        ans += count[m//2] != 0
        for i in range(1,m//2):
            if count[i] != 0 and count[m-i] != 0:
                if count[i] < count[m-i]:
                    count[i], count[m-i] = count[m-i], count[i]
                ans += 1 + max(0,(count[i] - (count[m-i]+1)))
            elif count[i] != 0 and count[m-i] == 0:
                ans += count[i]
            elif count[i] == 0 and count[m-i] != 0:
                ans += count[m-i]
            #print(i, ans)

    else:
        for i in range(1,m//2+1):
            if count[i] != 0 and count[m-i] != 0:
                if count[i] < count[m-i]:
                    count[i], count[m-i] = count[m-i], count[i]
                ans += 1 + max(0,(count[i] - (count[m-i]+1)))
            elif count[i] != 0 and count[m-i] == 0:
                ans += count[i]
            elif count[i] == 0 and count[m-i] != 0:
                ans += count[m-i]

    return ans

        
        

    #pass

for _ in range(test_case):
    n, m = rmi()
    A = ra()
    print(solve())