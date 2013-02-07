#!/usr/bin/env python3

def is_cancelable(a, b):
  sa = sorted(str(a))
  sb = sorted(str(b))

  if sa[0] == sb[0] and sa[0] != '0':
    new_a = int(sa[1])
    new_b = int(sb[1])
  elif sa[1] == sb[1]:
    new_a = int(sa[0])
    new_b = int(sb[0])
  else:
    return False

  if new_b == 0:
    return False

  return (a / b) == (new_a / new_b)

pa = 1
pb = 1

for a in range(10, 100):
  for b in range(a + 1, 100):
    if is_cancelable(a, b):
      pa *= a
      pb *= b

print(pa, pb)
