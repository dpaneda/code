#!/usr/bin/env python3

import math
import itertools

def t(n):
  return int((n * (n+1)) / 2)

triangles = set()

for n in range(1, 1000):
  triangles.add(t(n))

with open('words.txt', 'r') as f:
  words = f.read().split(",")

s = 0 

for word in words:
  wordvalue = 0 
  for letter in word:
    if letter != '"':
      wordvalue += ord(letter) - 64
  if wordvalue in triangles:
    s += 1

print(s)
