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
def isSubSequence(s,t):
    i = 0
    for j in range(len(t)):
        if t[j] == s[i]:
            i += 1
        
        if i == len(s):
            return True
    return False

def solve():
    S = s + p
    freq = collections.Counter(S)
    freq2 = collections.Counter(t)
    for c in freq2:
        if freq[c] < freq2[c]:
            return False
    if not isSubSequence(s,t):
        return False
    #print('test',isSubSequence('ab','acxb'))
    return True
    pass

for _ in range(test_case):
    s = rs()
    t = rs()
    p = rs()
    print('YES' if solve() else 'NO')