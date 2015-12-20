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

n = 2
for i in range(1, 10001):
  n = next_prime(n)

print(n)
