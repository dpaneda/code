#!/usr/bin/python2

import sys
import math

def Solve():
  l = map(int, sys.stdin.readline().split())

  N = l.pop(0)
  S = l.pop(0)
  p = l.pop(0)
  scores = l

  y = 0
  for sc in scores:
    med = sc / 3.0
  
    if (med == 0):
      y += (p == 0)
    elif math.ceil(med) >= p:
      y += 1
    elif (S > 0) and math.floor(med + 1.5) >= p:
      y += 1
      S -= 1

  return y

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %d" % (case, Solve())
