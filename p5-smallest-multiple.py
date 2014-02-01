import collections
def prime_decomposition(n):
  i = 2
  table = []
  while i * i <= n:
    while n % i == 0:
      n /= i
      table.append(i)
    i += 1
  if n > 1:
    table.append(n)

  cnt = collections.Counter()
  for t in table:
    cnt[t] += 1
  return cnt

n = 20
smallest = collections.Counter()
for i in xrange(2, n + 1):
  smallest = smallest | prime_decomposition(i)
print smallest
ans = 1
for k, v in smallest.items():
  ans *= pow(k, v)
print ans
