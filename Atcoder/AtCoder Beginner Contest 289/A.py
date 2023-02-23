import sys, math, itertools, functools, collections
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

s = rs()
tmp = s.replace('0','2')
tmp2 = tmp.replace('1','0')
tmp3 = tmp2.replace('2','1')
print(tmp3)