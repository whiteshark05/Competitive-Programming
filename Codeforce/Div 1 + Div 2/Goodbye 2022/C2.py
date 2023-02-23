from math import gcd

def can_make_coprime(a):
  n = len(a)
  g = a[0]
  for i in range(1, n):
    g = gcd(g, a[i])
  if g == 1:
    return "YES"
  for i in range(n):
    for j in range(i+1, n):
      if gcd(a[i]+g, a[j]+g) != 1:
        return "NO"
  return "YES"