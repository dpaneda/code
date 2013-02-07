#!/usr/bin/python2

import sys

def count_recycled_in(n, m, digits, low, high):
  total = 0
  r = n
  l = set()

  for i in xrange(0, digits):
    r = (r / 10) + m * (r % 10)
    if n != r and r >= low and r <= high:
      l.add(r)
  return len(l)

def Solve():
  [a, b] = map(int, sys.stdin.readline().split())

  total = 0
  flag = False
 
  digits = len(str(a))
  m = pow(10, len(str(a)) - 1)

  for n in xrange(a, b+1):
    total += count_recycled_in(n, m, digits, a, b)

  return total / 2

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %d" % (case, Solve())
