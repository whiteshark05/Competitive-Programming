s = input()
seen = set()
def isGood(s):
	count = 0
	for c in s:
		if c == '(':
			count += 1
		elif c == ')':
			count -= 1
		if count < 0: return False
	return count == 0

def solve():
	for i, c in enumerate(s):
		if c.isalpha():
			if c in seen: return False
			seen.add(c)
		elif c == '(':
			continue
		elif c == ')':
			for j in range(i - 1, -1, - 1)
				if isGood(s[j:i+1]):
					for k in range(j, i + 1):
						if s[k] in seen:
							seen.remove(s[k])
					break
	return True
print('Yes' if solve() else 'No')