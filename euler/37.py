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

def is_truncatable_prime(n):
  nstr = str(n)
  while len(nstr):
    if not is_prime(int(nstr)):
      return False
    nstr = nstr[1:]

  nstr = str(n)
  while len(nstr):
    if not is_prime(int(nstr)):
      return False
    nstr = nstr[:-1]

  return True

s = 0
for n in range(10, 1000000):
  if is_truncatable_prime(n):
    print(n)
    s += n

print(s)
