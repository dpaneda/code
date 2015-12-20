#!/usr/bin/env python3

import math

def is_prime(n):
  for m in range(2, 1 + int(math.sqrt(n))):
    if n % m == 0:
      return False
  return True

np = {}

def next_prime(n):
  if n in np:
    return np[n]
  n2 = n + 1
  while not is_prime(n2):
    n2 += 1
  np[n] = n2
  return n2

def factorize(n):
  factors = set()
  t = n
  p = 2
  while t != 1:
    if t % p == 0:
      t /= p
      factors.add(p)
    else:
      p = next_prime(p)
  return factors

SIZE = 4
sizes = []

#for n in range(1, 999999999):
#  s = factorize(n)
#  sizes.append(len(s))
#
#  if len(sizes) > SIZE:
#    sizes.pop(0)
#
#  if len(sizes) == SIZE and min(sizes) == SIZE and max(sizes) == SIZE:
#    break
#
#print(n - SIZE + 1)

print factorize(8532988864419328904093708339647638149986647745362001197797314494078355275500880794558784601)
