#!/usr/bin/env python3

import itertools


def d(n_str, d1, d2, d3):
  return int(n_str[d1-1] + n_str[d2-1] + n_str[d3-1])

s = 0

for number in itertools.permutations("0123456789"):
  if number[0] == "0":
    continue
  n_str = ""
  for digit in number:
    n_str += digit
  n = int(n_str)

  if (d(number, 2, 3, 4) % 2) == 0 \
    and (d(number, 3, 4, 5) % 3) == 0 \
    and (d(number, 4, 5, 6) % 5) == 0 \
    and (d(number, 5, 6, 7) % 7) == 0 \
    and (d(number, 6, 7, 8) % 11) == 0 \
    and (d(number, 7, 8, 9) % 13) == 0 \
    and (d(number, 8, 9, 10) % 17) == 0:
      s += n
      print(n)

print(s)
