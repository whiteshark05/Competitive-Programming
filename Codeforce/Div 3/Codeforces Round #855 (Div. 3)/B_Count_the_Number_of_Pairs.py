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
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = lower.upper()
    freq_lower = collections.Counter()
    freq_upper = collections.Counter()
    pair = 0
    ans = 0
    for c in s:
        if c.islower():
            freq_lower[c] += 1
        else:
            freq_upper[c] += 1
    pair = 0
    possible = 0
    for c1, c2 in zip(lower, upper):
        pair += min(freq_lower[c1], freq_upper[c2])
        possible += abs(freq_lower[c1] - freq_upper[c2]) // 2


    #print(freq_lower, freq_upper)
    return pair + min(possible, k)

    pass

for _ in range(test_case):
    n, k = rmi()
    s = rs()
    print(solve())