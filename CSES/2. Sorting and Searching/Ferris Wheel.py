rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

def solve():
    ans = 0
    a.sort()
    i, j = 0, n - 1
    while i <= j:
    	ans += 1
    	if a[i] + a[j] <= x:
    		i += 1
    	j -= 1

 
    return ans
    
 
n, x = rmi()
a = ra()
print(solve())
