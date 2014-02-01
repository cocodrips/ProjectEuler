e1 = 1
e2 = 2
sum = 0
while e2 < 4000000:
  if e2 %2 == 0:
    sum += e2

  next = e1 + e2
  e1 = e2
  e2 = next
print sum


# n = 4000000
# memo = [-1 for _ in xrange(n)]
# sum = 0
# print fi
#
# def fibo(i):
#   if memo[i] > -1:
#     return memo[i]
#   if i == 0:
#     return 1
#   if i == 1:
#     return 2
#
#   memo[i] = fibo(i-1) + fibo(i-2)
#   if memo[i] % 2 == 0:
#     sum += memo[i]
#   return memo[i]


