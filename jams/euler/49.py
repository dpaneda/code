#!/usr/bin/env python3

import math
import itertools

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

def same_digits(a, b, c):
  if b != a + 3330 or c != b + 3330:
    return False

  sa = sorted(str(a))
  sb = sorted(str(b))
  sc = sorted(str(c))

  return (sa == sb and sb == sc)

primes = []

n = 1000
while n < 10000:
  n = next_prime(n)
  primes.append(n)

for comb in itertools.combinations(primes, 3):
  if same_digits(*comb):
    print(comb)
