import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

rs  = lambda: input().strip()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

test_case = 1

#-------- DIFFERENT WAYS TO UNSTUCK ------------ 
# 1. Frequency/Value domain and Pigeon Hole Principle 
# 2. Search from end to start instead of start to end
# 3. Prefix Suffix
# 4. Brute force if small input size

def solve():
    
    pass

for _ in range(test_case):
    N, Q =rmi()
    players = collections.Counter()
    for _ in range(Q):
        e, d = rmi()
        if e == 1:
            if players[d] != 2:
                players[d] += 1
        elif e == 2:
            if players[d] != 2:
                players[d] = 2
        else:
            if players[d] == 2:
                print('Yes')
            else:
                print("No")
            
    