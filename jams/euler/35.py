#!/usr/bin/env python3

import math

def is_prime(n):
  if n < 0:
    n = -n

  for m in range(2, 1 + int(math.sqrt(n))):
    if n % m == 0:
      return False
  return True

def is_circular_prime(n):
  for d in str(n):
    if d == '0':
      return False

  for i in range(0, len(str(n))):
    if not is_prime(n):
      return False
    n = int(str(n)[1:] + str(n)[0])

  return True

s = 0
for n in range(2, 1000000):
  if is_circular_prime(n):
    s += 1

print(s)
