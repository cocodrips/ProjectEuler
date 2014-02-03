table = [2]
i = 3

while len(table) < 10001:
  j = 0

  while pow(table[j], 2) <= i:
    if i % table[j] == 0:
      break
    j +=1
  else:
    table.append(i)
  i += 2
print table[-1]

