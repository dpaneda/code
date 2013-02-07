#!/usr/bin/env python3

def is_pandigital(n):
  digits = []

  for digit in n:
    digits.append(int(digit))

  digits.sort()
  
  if len(digits) != 9:
    return False

  for i in range(0, 9):
    if digits[i] != i+1:
      return False

  return True

m = 0

for number in range(1, 20000):
  for n in range(1, 10):
    n_str = ""
    for i in range(1, n+1):
      n_str += str(number * i)

    if is_pandigital(n_str):
      if int(n_str) > m:
        m = int(n_str)

print(m)
