#!/usr/bin/env python3

import math
import itertools

def is_prime(n):
  for m in range(2, 1 + int(math.sqrt(n))):
    if n % m == 0:
      return False
  return True

nprimes = 0
ntotal = 1
number = 1

for circle in range(1, 1000000):
  for i in range(0, 4):
    number += circle * 2
    ntotal += 1
    if is_prime(number):
      nprimes += 1
  if (nprimes / ntotal) < 0.10:
    break

print(circle * 2 + 1)
print(nprimes / ntotal)
