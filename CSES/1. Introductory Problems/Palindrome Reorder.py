import collections
s = input()
freq = collections.Counter(s)
count = 0
front = ''
back = ''
oddchar = ''
for k, v in freq.items():
	if v % 2 == 1:
		oddchar = k
		count += 1
	front += k * (v//2)
	back = k * (v//2) + back
 
 
if count > 1: print("NO SOLUTION")
print(front + oddchar + back)