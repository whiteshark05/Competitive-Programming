
# Online Python - IDE, Editor, Compiler, Interpreter

a = [1, 2 ,3 ,3 ,3, 4, 4]
n = len(a)
def bs(a, l, r, target):
    ans = -1
    while l <= r:
        m = (l + r) // 2
        if a[m] == target: 
            ans = m
            l = m + 1
        elif a[m] < target:
            l = m + 1
        else:
            r = m - 1
    return ans
    
def quicksort(xs):
    if xs: 
        pivot = xs[0]
        below = [i for i in xs[1:] if i > pivot] 
        above = [i for i in xs[1:] if i <= pivot]
        return quicksort(below) + [pivot] + quicksort(above)
    else: 
        return xs 
        
def fsort(a):
    l, r = 0, 0
    while l < len(a): # O(N)
        r = bs(a, l, n-1, a[l])  # O(logN) -> O(NlogN)
        f = r - l + 1
        for _ in range(l, r+1):
            a[l] += 10000*f
            l += 1
        l = r + 1
    
    a = quicksort(a) # O(NlogN)
    
    for i in range(len(a)): #O(N)
        a[i] %= 10000
    
    return a
    
print(fsort(a)) #[3, 3, 3, 4, 4, 2, 1]




