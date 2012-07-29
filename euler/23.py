#!/usr/bin/env python3

from itertools import combinations_with_replacement, combinations

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

  s = 1
  for i in full_factors:
    s += i
    
  return s

def is_abundant(n):
  return sum_factors(n) > n

abundants = []
all_numbers = set()

for n in range(12, 28124):
  all_numbers.add(n)
  if is_abundant(n):
    abundants.append(n)

for comb in combinations_with_replacement(abundants, 2):
  s = comb[0] + comb[1]
  if s in all_numbers:
    all_numbers.remove(s)

s = 0
for n in all_numbers:
  s += n

for n in range(1, 12):
  s += n

print(s)
