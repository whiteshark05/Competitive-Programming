import collections
s = input()
n = len(s)
s = sorted(list(s))
ans = []
counter = collections.Counter(s)
def dfs(path, counter):
	if len(path) == len(s):
		ans.append(''.join(path[::]))
	for c in counter:
		if counter[c] > 0:
			dfs(path+[c], counter - collections.Counter({c:1}))
		
dfs([], counter)
print(len(ans))
for s in ans:
	print(s)