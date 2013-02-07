#!/usr/bin/env python3

def same_digits(a, b):
  sa = sorted(str(a))
  sb = sorted(str(b))
  return sa == sb

def check_6x(n):
  for i in range(1, 7):
    if not same_digits(n, n*i):
      return False

  return True

for n in range(1, 10000000000):
  if check_6x(n):
    break

print(n)
