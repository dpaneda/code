#!/usr/bin/env python3

import math

def is_prime(n):
  if n == 1:
    return False

  if n < 0:
    n = -n

  for m in range(2, 1 + int(math.sqrt(n))):
    if n % m == 0:
      return False

  return True

def is_goldbach(n):
  for a in range(2, n):
    for b in range (1, int(math.sqrt(n))):
      if is_prime(a) and (a + 2*b*b) == n:
        return True
  return False

for n in range(3, 10000):
  if not is_prime(n) and n % 2 and not is_goldbach(n):
    break    

print(n)
