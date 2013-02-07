#!/usr/bin/env python3

def is_pandigital_product(a, b, c):
  digits = []

  for digit in str(a) + str(b) + str(c):
    digits.append(int(digit))

  if len(digits) != 9:
    return False

  digits.sort()
  
  for i in range(0, 9):
    if digits[i] != i+1:
      return False

  return True

terms = set()

for a in range(1, 100):
  for b in range(10, 9000):
    if is_pandigital_product(a, b, a*b):
      terms.add(a*b)

s = 0
for term in terms:
  s += term

print(s)

