import sys, math, itertools, functools, collections
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

testcases = int(input())
 
 
def solve():
    length, k = map(int, input().split())
    s = input()
    t = input()
 
    par = [i for i in range(length)]
    size = [1 for i in range(length)]
    def find(n):
        if par[n] != n:
            par[n] = find(par[n])
        return par[n]
 
    def union(n1, n2):
        p1 = find(n1)
        p2 = find(n2)
        if p1 == p2:
            return
        if size[p1] >= size[p2]:
            par[p2] = p1
            size[p1] += size[p2]
        else:
            par[p1] = p2
            size[p2] += size[p1]
   
    for i, char in enumerate(s):
        if i + k < length:
            union(i, i+k)
 
        if i + k + 1 < length:
            union(i, i+k+1)
    counts = [[0 for x in range(26)] for i in range(length)]
    for i, char in enumerate(s):
        p = find(i)
        counts[p][ord(char) - ord('a')] += 1
    for i, char in enumerate(t):
 
        p = find(i)
 
        if counts[p][ord(char) - ord('a')] == 0:
            print("no")
            return
        counts[p][ord(char)-ord('a')] -= 1
    print("yes")
 
 
for case in range(testcases):
    solve()