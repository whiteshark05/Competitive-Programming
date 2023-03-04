#! /usr/bin/env python3
 
"""
# Question 37
 
Anubhav has a crush on Anu. Therefore he like the letters A, N and U the most.
He likes those strings which consist of only A, N, U.
According to him, the strings containing A, N and U only are "LOVABLE" if they
contain either of these patterns:
1) ANU
2) AUN
3) NAU
4) NUA
5) UAN
6) UNA
He asks you to find out how many LOVABLE strings there are of length N.
Note: Assume all strings are made of A, N, U. Consider all other alphabets as
non-existent.
 
Input format:
First line contains T, the number of test cases.
Next T lines contain a single integer N, denoting the length of the string.
 
Output format:
Output the count of LOVABLE strings of length N in a single line for each test
case.
 
Constraints:
1 <= T <= 30
1 <= N <= 30
 
Test Case
Input
30
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
 
Output
0
0
6
30
120
432
1470
4830
15504
48960
152790
472638
1452360
4440240
13521486
41049150
124317600
375777792
1134153510
3418925790
10296528024
30985550640
93188335710
180124341278
841723375920
2528430166080
7593160926966
22798483676670
68441323250280
205434715087152
 
https://redd.it/11bl3rd
"""

def dp(i, j, k):
    if i == 0:
        return 1
    
    count = 0
    for c in ['A','N','U']:
        



print(dp(4,'',''))