def is_prime(n):
  if n == 2:
    return True

  i = 3
  while i * i < n:
    if n % i == 0:
      return False
    i += 2
  return True


def prime_decomposition(n):
  i = 2
  table = []
  while i * i < n:
    while n % i == 0:
      n /= i
      table.append(i)
    i += 1
  table.append(n)
  return table

if __name__ == '__main__':
  n = int(raw_input())
  print prime_decomposition(n)




