#!/usr/bin/env python3

import math

def is_prime(n):
  if n < 0:
    n = -n

  for m in range(2, int(math.sqrt(n))):
    if n % m == 0:
      return False
  return True

better_tuple = (0, 0, 0)

for a in range(-1000, 1000):
  for b in range(-1000, 1000):
    primes = 0
    for n in range(0, 1000):
      posible_prime = n * n + b*n + a
      if is_prime(posible_prime):
        primes += 1
      else:
        break
    if primes > better_tuple[2]:
      better_tuple = (a, b, primes)

print(better_tuple)
print(better_tuple[0] * better_tuple[1])
