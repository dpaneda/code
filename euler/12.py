#!/usr/bin/env python3

from itertools import combinations

def is_prime(n):
  for m in range(2, n):
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
  factors = []
  t = n
  p = 2
  while t != 1:
    if t % p == 0:
      t /= p
      factors.append(p)
    else:
      p = next_prime(p)
  return factors

def count_factors(n):
  factors = factorize(n)
  full_factors = set(factors)

  if len(factors) == 1:
    return 2

  for c in range(2, len(factors)):
    for comb in combinations(factors, c):
      prod = 1
      for number in comb:
        prod *= number
      full_factors.add(prod)

  return len(full_factors) + 2

n = 1
i = 1

while count_factors(n) < 500:
  i += 1
  n += i

print(n)
