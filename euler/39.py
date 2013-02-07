#!/usr/bin/env python3

def is_right_triangle(a, b, c):
  return a**2 == (b**2 + c**2)

def number_of_solutions(n):
  sols = 0
  for a in range(1, n):
    for b in range(1, n - a + 1):
      c = n - a - b
      if is_right_triangle(a, b, c):
        sols += 1
  return sols

m = (0, 0)
for n in range(1, 1001):
  print(n)
  ns = number_of_solutions(n)
  if ns > m[0]:
    m = (ns, n)

print(m)
