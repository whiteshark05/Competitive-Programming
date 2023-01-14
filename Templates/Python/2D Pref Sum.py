pref = [[0 for x in range(C)] for y in range (R)]
answer = [[0 for x in range(C)] for y in range (R)]
"""
A B
C D

pref = A + D - B - C
range query = A + D - B - C

"""
for i in range(R):
    for j in range(C):
        if i==0:
            pref[i][j]=pref[i][j-1]+mat[i][j]
        elif j==0:
            pref[i][j]=pref[i-1][j]+mat[i][j]
        else:
            pref[i][j]=pref[i-1][j]+pref[i][j-1]-pref[i-1][j-1]+mat[i][j]

for i in range(R):
    for j in range(C):
        A=pref[min(R-1,i+K)][min(C-1,j+K)]
        B=pref[max(0,i-K-1)][max(0,j-K-1)] if (i-K-1)>=0 and (j-K-1)>=0 else 0
        C=pref[min(R-1,i+K)][max(0,j-K-1)] if (j-K-1)>=0 else 0
        D=pref[max(0,i-K-1)][min(C-1,j+K)] if (i-K-1)>=0 else 0