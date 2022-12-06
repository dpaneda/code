#! /usr/bin/env python
import sys,functools

def value(c):
    if c.islower():
        return ord(c) - 96
    else:
        return ord(c) - 38

c = 0
lines = [l.strip() for l in sys.stdin]
while lines:
    items = functools.reduce(lambda s1,s2: s1 & s2, map(set, lines[:3]))
    c += value(items.pop())
    lines = lines[3:]
print(c)
