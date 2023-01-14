"""
https://www.hackerearth.com/practice/math/combinatorics/inclusion-exclusion/practice-problems/algorithm/count-numbers-7/
TC IP:
2 1
2 3
1 10
OP:
7
"""
K, T = map(int, input().split())
primes = list(map(int, input().split()))

while T:
    A, B = map(int, input().split())
    #Generate all subsets of primes. Done
    #Get the product p of subsets.
    #Find the sign 
    #Return A//p
    def find(N):
        ans = 0
        def intersectionCardinality(indices):
            p = 1
            for num in indices:
                p *= num
            return p


        for b in range(1, 1 << K): #Total number of subsets (2^K)
            indices = []
            for k in range(K): #Index of the subset (K)
                if b & (1 << k):
                    indices.append(primes[k])
                    
            cardinality = intersectionCardinality(indices)
            if len(indices) % 2 == 1:
                ans += N//cardinality
            else:
                ans -= N//cardinality
        return ans
        
    print(find(B) - find(A-1))
    T-=1