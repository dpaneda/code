#!/usr/bin/env python3

longest = (0, 0)

for n in range(2, 1000001):
  m = n
  chain = 1

  while m != 1:
    chain += 1
    if m % 2:
      m = 3 * m + 1
    else:
      m /= 2

  if chain > longest[1]:
    longest = (n, chain)

print(longest)
