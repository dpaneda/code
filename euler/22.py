#!/usr/bin/env python3

with open('names.txt', 'r') as f:
  names = f.read().split(",")

names.sort()

s = 0
i = 0

for name in names:
  i += 1
  namevalue = 0
  for letter in name:
    if letter != '"':
      namevalue += ord(letter) - 64
  s += namevalue * i

print(s)
