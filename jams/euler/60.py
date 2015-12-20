#!/usr/bin/env python3

import math
import itertools

def is_prime(n):
  for m in xrange(2, 1 + int(math.sqrt(n))):
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

def remarkable(primes):
  for comb in itertools.permutations(primes, 2):
    n = int(str(comb[0]) + str(comb[1]))
    if not is_prime(n):
      return False
  return True


primes = []

n = 1

while n < 50000:
  n = next_prime(n)
  primes.append(n)

lowest = 999999999
num_comb = 0

for comb in itertools.combinations(primes, 2):
  if remarkable(comb):
    num_comb += 1
    if sum(comb) < lowest:
      print(lowest)
      lowest = sum(comb)

print(lowest)
print(num_comb)

