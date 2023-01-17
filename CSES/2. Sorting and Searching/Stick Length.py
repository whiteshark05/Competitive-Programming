rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

def solve():
    n = len(a)
    s = sum(a)
    avg = s/n
    upper = (s + n - 1)//n
    lower = s // n 
    cur = 0
    ans = 0
    count = 0
    for num in a[:-1]:
    	count += 1
    	cur += num
    	cur_avg = cur/count
    	if cur_avg > avg:
    		ans += abs(lower - num)
    	elif cur_avg == avg:
    		continue
    	else:
    		ans += abs(upper - num)
    	
    ans += abs(s - cur) 
    return ans
    
n = ri()
a = ra()

print(solve())