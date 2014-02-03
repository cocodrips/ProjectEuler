n = 5

str = raw_input()
l = map(int, list(str))
maxi = 1

for i in xrange(0, len(l) - n + 1):
  multi = 1
  for j in xrange(n):
    multi *= l[i + j]
  maxi = max(maxi, multi)

print maxi

