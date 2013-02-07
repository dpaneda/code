#!/usr/bin/python

import sys

def mergesort(l):
  n = len(l)
  
  if n <= 1:
    return l, 0

  middle = int(n / 2)
  
  l1, inv1 = mergesort(l[:middle])
  l2, inv2 = mergesort(l[middle:])  
  
  i = 0
  j = 0

  ls = []
  inv = inv1 + inv2

  while len(ls) < n:
    if i >= len(l1):
      ls += l2[j:]
      break

    if j >= len(l2):
      ls += l1[i:]
      break

    if l1[i] <= l2[j]:
      ls.append(l1[i])
      i += 1
    else:
      ls.append(l2[j])
      j += 1
      inv += len(l1) - i

  return ls, inv

l = []
for number in sys.stdin:
  l.append(int(number))

ls, inv = mergesort(l)
print(inv)
