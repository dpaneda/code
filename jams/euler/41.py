#!/usr/bin/env python3

import math
import itertools

def is_prime(n):
  if n == 1:
    return False

  if n < 0:
    n = -n

  for m in range(2, 1 + int(math.sqrt(n))):
    if n % m == 0:
      return False

  return True

def is_pandigital(n, r):
  digits = []

  for digit in str(n):
    digits.append(int(digit))

  digits.sort()
  
  if len(digits) != r:
    return False

  for i in range(0, r):
    if digits[i] != i+1:
      return False

  return True

m = 0
r = 4

for r in range(4, 10):
  cad = ""
  for d in range(1, r + 1):
    cad += str(d)

  for number in itertools.permutations(cad):
    n_str = ""
    for digit in number:
      n_str += digit
    n = int(n_str)

    if is_pandigital(n, r) and is_prime(n):
      if n > m:
        m = n

print(m)
