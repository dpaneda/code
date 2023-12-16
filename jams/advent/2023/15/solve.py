#! /usr/bin/env python

import re
from dataclasses import dataclass

@dataclass
class Op():
    label : str
    op : str
    focal : int = 0

    def __init__(self, s):
        r = re.match(r"(\w+)([=-])(\d+)?", s)
        self.label, self.op = r.groups()[:2]
        if self.op == '=':
            self.focal = int(r.group(3))

def hsh(s):
    n = 0
    for c in s:
        n += ord(c)
        n *= 17
        n %= 256
    return n

n = 0
slots = {}
for s in input().split(','):
    h = hsh(s)
    n += h
    
    op = Op(s)
    box = hsh(op.label)
    found = -1
    l = slots.get(box, [])
    for i, op2 in enumerate(l):
        if op2.label == op.label:
            found = i
    if found >= 0:
        l.pop(found)
        if op.op == '=':
            l.insert(found, op)
    elif op.op == '=':
        l.append(op)
    slots[box] = l


focus_power = 0
for box, v in slots.items():
    for i, lens in enumerate(v):
        focus_power += (box + 1) * (i + 1) * lens.focal

print(n)
print(focus_power)
