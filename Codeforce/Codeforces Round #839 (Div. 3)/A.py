t = int(input())
a= []

def solve(a,b):
    return a+b

for _ in range(t):
    a, b = map(int, input().split('+'))
    print(solve(a,b))
    