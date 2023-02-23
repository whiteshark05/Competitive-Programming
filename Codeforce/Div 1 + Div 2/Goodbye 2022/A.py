import collections, heapq, itertools, math
groupby = itertools.groupby
rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
 
def solve():
    heapq.heapify(a)
    for i in range(m):
        heapq.heappop(a)
        heapq.heappush(a, b[i])
    return sum(a)
 
for t in range(ri()):
    n, m  = rmi()
    a = ra()
    b = ra()
    ans = solve()
    print ("{}".format(ans))