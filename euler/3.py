#!/usr/bin/env python3

def is_prime(n):
  for m in range(2, n):
    if n % m == 0:
      return False
  return True

def next_prime(n):
  n += 1
  while not is_prime(n):
    n += 1
  return n

def factorize(n):
  factors = set()
  t = n
  p = 2
  while t != 1:
    if t % p == 0:
      t /= p
      factors.add(p)
    else:
      p = next_prime(p)

  return factors
    
print(factorize(600851475143))
