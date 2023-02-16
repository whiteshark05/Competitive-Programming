import collections, heapq, itertools, math
groupby = itertools.groupby
rs  = lambda: input()
ri  = lambda: int(input())
rm  = lambda: map(int, input().split())
rai = lambda: [int(x) for x in input().split()]
 
def solve(y,x):
    z = max(x,y)
    m = z*(z-1)+1
    #print(z,m)
    if z%2:
        if x>y: return m+(z-y)
        else: return m-(z-x)
    else:
        if x>y: return m-(z-y)
        else: return m+(z-x)
 
for t in range(ri()):
    y,x = rm()
    ans = solve(y,x)
    print ("{}".format(ans))