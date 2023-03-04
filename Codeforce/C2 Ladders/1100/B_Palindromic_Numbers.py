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
    #s = str(num)
    for d in range(1, 10):
        target = str(d) * (n+1)
        new_num = int(target) - x
        str_new_num = str(new_num)
        #print(new_num)
        if len(str_new_num) == len(str(x)):
            return new_num

        target2 = str(d) * (n)
        new_num2 = int(target2) - x
        str_new_num2 = str(new_num2)
        #print(new_num)
        if len(str_new_num2) == len(str(x)):
            return new_num2

for _ in range(test_case):
    n = ri()
    x = ri()
    print(solve())