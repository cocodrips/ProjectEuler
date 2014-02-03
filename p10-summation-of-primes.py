def prime_table(n):
  list = [True for _ in xrange(n + 1)]
  i = 2
  while i * i <= n:
    if list[i]:
      j = i + i
      while j <= n:
        list[j] = False
        j += i
    i += 1

  table = [i for i in xrange(n + 1) if list[i] and i >= 2]
  return table

table = prime_table(2000000)
sum = 0
for t in table:
  sum += t
print sum