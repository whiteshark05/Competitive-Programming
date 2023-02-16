#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
from collections import defaultdict as ddic
from itertools import combinations

# region fastio
 
BUFSIZE = 8192
 
 
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 
 
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

rs  = lambda: input()
ri  = lambda: int(input())
rmi  = lambda: map(int, input().split())
ra = lambda: [int(x) for x in input().split()]
pa = lambda x: print (" ".join(map(str, x)))
 
def solve():
	ans = 0
	count = 0
	index0 = 0
	index1 = n - 1
	flag = False
	for i, num in enumerate(a):
		if num == 1:
			count += 1
			index1 = i
		else:
			if not flag:
				index0 = i
				flag = True
			ans += count

	ans1, ans2 = 0, 0
	a1 = a[:index0] + [1] + a[index0+1:]
	a2 = a[:index1] + [0] + a[index1+1:]
	#print(a, a1, a2)
	count = 0
	for i, num in enumerate(a1):
		if num == 1:
			count += 1
		else:
			ans1 += count
	count = 0
	for i, num in enumerate(a2):
		if num == 1:
			count += 1
		else:
			ans2 += count

	return max(ans, ans1, ans2)
    
 
t = ri()
for _ in range(t):
	n = ri()
	a = ra()
	print(solve())