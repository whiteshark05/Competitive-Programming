rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))

def solve():
    tmp = 0
    res = 0
    count = 0
    for num in a:
        if num == 1:
            count += 1
        else:
            tmp += count
        #res = max(res, ans - )
    print(tmp)
    z, o = [0], [0]
    for i in reversed(range(len(a))):
        if a[i] == 0:
            z.append(z[-1] + 1)
        else:
            z.append(z[-1])
    z = z[::-1]
    
    for i in range(len(a)):
        if a[i] == 1:
            o.append(o[-1] + 1)
        else:
            o.append(o[-1])

    diff = 0
    print(z, o)
    for i in range(len(z)):
        if a[]
        diff = max(diff, o[i] - z[i])
    print(diff)
    return tmp + diff
    
for t in range(ri()):
    n = ri()
    a = ra()
    print(solve())