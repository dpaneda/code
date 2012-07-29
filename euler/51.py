#!/usr/bin/env python3

import math
import itertools
import sys

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

n = 1000
primes = []

while n < 40000000:
  n = next_prime(n)
  primes.append(n)

print("Done")

def check_family(n):
  ns = list(str(n))

  for a in range(0, len(ns)):
    for b in range(a + 1, len(ns)):
      rp = 0
      for replacement in range(0, 10):
        si = ns[:a] + [str(replacement)] + ns[a+1:b] + [str(replacement)] + ns[b+1:]
        i = int(''.join(p for p in si))
        if i in np:
          if not rp:
            first = i
          rp += 1
      if rp == 8:
        print(first)
        sys.exit(0)
       

for n in primes:
  check_family(n)
