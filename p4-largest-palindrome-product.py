def is_palindrome(n):
  n_list = list(str(n))
  for i in xrange(len(n_list) / 2):
    if n_list[i] != n_list[len(n_list) - i - 1]:
      return False
  return True


pair = ()
sum = []
for i in xrange(100, 1000):
  for j in xrange(i, 1000):
    if is_palindrome(i * j):
      sum.append(i*j)
sum.sort()
print sum