T = int(input())
for _ in range(T):
    N = int(input())
    for p in range(2, int(N**(1/3))+1):
        if N % p == 0:
            break;
    if N % p ** 2 == 0:
        print(p, int(N//p**2))
    else:
        print(int((N//p) ** (1/2)),p)