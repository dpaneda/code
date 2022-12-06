#! /usr/bin/env python
import sys

def value(c):
    if c.islower():
        return ord(c) - 96
    else:
        return ord(c) - 38

c = 0
for l in sys.stdin.readlines():
    middle = len(l) // 2
    item = (set(l[:middle]) & set(l[middle:])).pop()
    c += value(item)
print(c)
