#!/usr/bin/python2

import sys

def Solve():
  char_map = {'a': 24,
              'b': 6, 
              'c': 2, 
              'd': 15, 
              'e': 10, 
              'f': -3, 
              'g': 15, 
              'h': 16, 
              'i': -5, 
              'j': 11, 
              'k': -2, 
              'l': -5, 
              'm': -1, 
              'n': -12, 
              'o': -4, 
              'p': 2, 
              'q': 9,
              'r': 2, 
              's': -5, 
              't': 3, 
              'u': -11, 
              'w': -17, 
              'v': -6, 
              'y': -24, 
              'x': -11,
              'z': -9
              }
  out = ""
  for c in sys.stdin.readline().strip():
    if c in char_map:
      c = chr( ord(c) + char_map[c])
    out += c
  return out

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s " % (case, Solve())
