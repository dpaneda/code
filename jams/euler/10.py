#!/usr/bin/env python3

import math

def is_prime(n):
  for m in range(2, int(math.sqrt(n))):
    if n % m == 0:
      return False
  return True

def next_prime(n):
  n += 1
  while not is_prime(n):
    n += 1
  return n

n = 2
p = 0

MAX = 2000001

numbers = []
primes = []

for n in range(0, MAX):
  numbers.append(n)
  primes.append(1)

primes[0] = 0
primes[1] = 0

for n in numbers:
  if primes[n]:
    primes[n] = is_prime(n)
    if primes[n]:
      m = 2 * n
      while m < MAX:
        primes[m] = 0
        m += n

s = 0
for i in range(0, MAX):
  if primes[i]:
    s += i

print(s)
