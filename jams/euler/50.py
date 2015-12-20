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

primes = []

n = 1
while n < 1000000:
  n = next_prime(n)
  primes.append(n)

maxlen = 0
maxprime = 0

for a in range(0, len(primes)):
  for b in range(a + 1, len(primes)):
    if b - a > maxlen:
      s = sum(primes[a:b])
      if s in np:
        maxlen = b - a
        maxprime = s
        print(primes[a:b])
        print(s)
