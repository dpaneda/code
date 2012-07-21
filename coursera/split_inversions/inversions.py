#!/usr/bin/python

import sys

def count_inversions(l, start, end):
  n = end - start
  
  if n <= 1:
    return 0

  middle = start + int(n / 2)
  
  inv1 = count_inversions(l, start, end - middle)
  inv2 = count_inversions(l, start + middle, end)  
  
  inv = inv1 + inv2

  c = 0
  k = 0
  
  for n in l[start:middle]:
    if n > middle:
      c += 1

  for n in l[middle:end]:
    if n < middle:
      k += 1

  inv += int((k * n * c) / 2)

  return inv

l = []
for number in sys.stdin:
  l.append(int(number))

inv = count_inversions(l, 0, len(l))
print(inv)
