
def pythagorean():
  for a in xrange(1,999):
    for b in xrange(a, 999):
      c = 1000 - a - b
      if pow(c, 2) == pow(a, 2) + pow(b, 2):
        return a * b * c

print pythagorean()