#template taken from https://codeforces.com/contest/1703/submission/164030692 - Author mkawa2
class DefaultDict:
    def __init__(self, default=None):
        self.default = default
        self.x = random.randrange(1, 1 << 31)
        self.dd = defaultdict(default)
    def __repr__(self):
        return "{"+", ".join(f"{k ^ self.x}: {v}" for k, v in self.dd.items())+"}"
    def __eq__(self, other):
        for k in set(self) | set(other):
            if self[k] != other[k]: return False
        return True
    def __or__(self, other):
        res = DefaultDict(self.default)
        for k, v in self.dd: res[k] = v
        for k, v in other.dd: res[k] = v
        return res
    def __len__(self):
        return len(self.dd)
    def __getitem__(self, item):
        return self.dd[item ^ self.x]
    def __setitem__(self, key, value):
        self.dd[key ^ self.x] = value
    def __delitem__(self, key):
        del self.dd[key ^ self.x]
    def __contains__(self, item):
        return item ^ self.x in self.dd
    def items(self):
        for k, v in self.dd.items(): yield (k ^ self.x, v)
    def keys(self):
        for k in self.dd: yield k ^ self.x
    def values(self):
        for v in self.dd.values(): yield v
    def __iter__(self):
        for k in self.dd: yield k ^ self.x
class CounterInt(DefaultDict):
    def __init__(self, aa=[]):
        super().__init__(int)
        for a in aa: self.dd[a ^ self.x] += 1
    def __add__(self, other):
        res = CounterInt()
        for k in set(self) | set(other):
            v = self[k]+other[k]
            if v > 0: res[k] = v
        return res
    def __sub__(self, other):
        res = CounterInt()
        for k in set(self) | set(other):
            v = self[k]-other[k]
            if v > 0: res[k] = v
        return res
    def __and__(self, other):
        res = CounterInt()
        for k in self:
            v = min(self[k], other[k])
            if v > 0: res[k] = v
        return res
    def __or__(self, other):
        res = CounterInt()
        for k in set(self) | set(other):
            v = max(self[k], other[k])
            if v > 0: res[k] = v
        return res
class Set:
    def __init__(self, aa=[]):
        self.x = random.randrange(1, 1 << 31)
        self.st = set()
        for a in aa: self.st.add(a ^ self.x)
    def __repr__(self):
        return "{"+", ".join(str(k ^ self.x) for k in self.st)+"}"
    def __len__(self):
        return len(self.st)
    def add(self, item):
        self.st.add(item ^ self.x)
    def discard(self, item):
        self.st.discard(item ^ self.x)
    def __contains__(self, item):
        return item ^ self.x in self.st
    def __iter__(self):
        for k in self.st: yield k ^ self.x
    def pop(self):
        return self.st.pop() ^ self.x
    def __or__(self, other):
        res = Set(self)
        for a in other: res.add(a)
        return res
    def __and__(self, other):
        res = Set()
        for a in self:
            if a in other: res.add(a)
        for a in other:
            if a in self: res.add(a)
        return res
 
 
#https://leetcode.com/problems/create-sorted-array-through-instructions/discuss/1245397/C%2B%2BJavaPython-Binary-Indexed-Tree-Feel-free-to-reuse   
class BIT:
    def __init__(self, size):
        self.bit = [0] * (size + 1)
 
    def getSum(self, idx):  # Get sum in range [0..idx], 1-based indexing
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & (-idx)
        return s
 
    def getSumRange(self, left, right):  # left, right inclusive, 1-based indexing
        return self.getSum(right) - self.getSum(left - 1)
 
    def addValue(self, idx, val):  # 1-based indexing
        while idx < len(self.bit):
            self.bit[idx] += val
            idx += idx & (-idx)
            
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None
 
    def addWord(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.word = "*"
 
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n
 
    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a
 
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
 
            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]
 
    def set_size(self, a):
        return self.size[self.find(a)]
 
    def __len__(self):
        return self.num_sets
    
class LazySegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the lazy segment tree with data"""
        self._default = default
        self._func = func
 
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        self._lazy = [0] * (4 * _size)
 
        self.data = [default] * (4 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])
 
    def __len__(self):
        return self._len
 
    def _push(self, idx):
        """push query on idx to its children"""
        # Let the children know of the queries
        q, self._lazy[idx] = self._lazy[idx], 0
 
        self._lazy[2 * idx] += q
        self._lazy[2 * idx + 1] += q
        self.data[2 * idx] += q
        self.data[2 * idx + 1] += q
 
    def _update(self, idx):
        """updates the node idx to know of all queries applied to it via its ancestors"""
        for i in reversed(range(1, idx.bit_length())):
            self._push(idx >> i)
 
    def _build(self, idx):
        """make the changes to idx be known to its ancestors"""
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1]) + self._lazy[idx]
            idx >>= 1
 
    def add(self, start, stop, value):
        """lazily add value to [start, stop)"""
        start = start_copy = start + self._size
        stop = stop_copy = stop + self._size
        while start < stop:
            if start & 1:
                self._lazy[start] += value
                self.data[start] += value
                start += 1
            if stop & 1:
                stop -= 1
                self._lazy[stop] += value
                self.data[stop] += value
            start >>= 1
            stop >>= 1
 
        # Tell all nodes above of the updated area of the updates
        self._build(start_copy)
        self._build(stop_copy - 1)
 
    def query(self, start, stop, default=0):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size
 
        # Apply all the lazily stored queries
        self._update(start)
        self._update(stop - 1)
 
        res = default
        while start < stop:
            if start & 1:
                res = self._func(res, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self.data[stop])
            start >>= 1
            stop >>= 1
        return res
 
    def __repr__(self):
        return "LazySegmentTree({0})".format(self.data)
    
#Author: beethoven97
def sieve(n):
    prim = [False] * (n + 1)
    ret = []
    for i in range(2, n + 1):
        if not prim[i]:
            ret.append(i)
            for j in range(i, n + 1, i):
                prim[j] = 1
 
    return ret
 
# find smallest prime factor for all numbers <= n
class Prime:
    
    def __init__(self,n):
        self.n = n
        self.smallest_prime = [0]*(self.n+5)
 
        for i in range(2, self.n + 1):
            if not self.smallest_prime[i]:
                for j in range(i, self.n + 1, i):
                    self.smallest_prime[j] = i
                    
    def factorise(self,num):
        
        ans = []
        while self.smallest_prime[num] != 0:
            k = self.smallest_prime[num]
            ans.append(k)
            while num % k == 0:
                num //= k
                
        return ans
    
 
# Function to find the value of
# P * Q^-1 mod 998244353 (G4G)
def mod_inverse(p, q, mod):
    
    expo = 0
    expo = mod - 2
 
    # Loop to find the value
    # until the expo is not zero
    while (expo):
 
        # Multiply p with q
        # if expo is odd
        if (expo & 1):
            p = (p * q) % mod
        q = (q * q) % mod
 
        # Reduce the value of
        # expo by 2
        expo >>= 1
 
    return p
 
#PyRival
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to
 
    return wrappedfunc
 
#Author: huikang
def remove_consecutive_duplicates(lst):
    res = []
    for x in lst:
        if res and x == res[-1]:
            continue
        res.append(x)
    return res
 
#nmax = 2000000
#fact = [1] * (nmax+1)
#for i in range(2, nmax+1):
#    fact[i] = fact[i-1] * i % MOD
#    
#inv = [1] * (nmax+1)
#inv[-1] = pow(fact[-1], MOD-2, MOD)
#for i in range(nmax-1, 0, -1):
#    inv[i] = inv[i+1] * (i+1) % MOD
 
 
#def C(n, m):
#    return fact[n] * inv[m] % MOD * inv[n-m] % MOD if 0 <= m <= n else 0
 
def sumtoN(n):
    return ((n)*(n+1)) // 2
 
def powerOf2(n):
    return n > 0 and n & (n-1) == 0
 
def query(a,b):
    print("? {} {}".format(a,b), flush=True)
    response = int(input())
    return response
 
def alert(num):
    print("! {}".format(num), flush=True)
 
# d4 = [(0, 1), (-1, 0), (0, -1), (1, 0)]
# d8 = [(0, 1), (-1, 0), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
#mod = 1000000007