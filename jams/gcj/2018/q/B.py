#!/usr/bin/python2

import sys
import random

def trouble_sort(l):
    done = False
    while not done:
      done = True
      for i in xrange(0, len(l) - 2):
        if l[i] > l[i+2]:
          done = False
          l[i], l[i+2] = l[i+2], l[i]

def fast_trouble(l):
    a, b = l[::2], l[1::2]
    a.sort()
    b.sort()
    l = []
    for i in xrange(0, max(len(a), len(b))):
        l.append(a[i])
        if i < len(b):
            l.append(b[i])
    return l

def solve():
    raw_input()
    l = map(int, raw_input().split())
    l = fast_trouble(l)
    for i in xrange(0, len(l) - 1):
        if l[i] > l[i+1]:
            return i
    return "OK"


num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print("Case #{0}: {1}".format(case, solve()))
