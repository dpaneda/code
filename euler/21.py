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

def sum_factors(n):
  factors = factorize(n)
  full_factors = set(factors)

  if len(factors) == 1:
    return 1

  for c in range(2, len(factors)):
    for comb in combinations(factors, c):
      prod = 1
      for number in comb:
        prod *= number
      full_factors.add(prod)

  s = 0
  for i in full_factors:
    s += i
    
  return s + 1

s = 0
for n in range(2, 10000):
  d = sum_factors(n)
  if (d != n and sum_factors(d) == n):
    s += n

print(s)
