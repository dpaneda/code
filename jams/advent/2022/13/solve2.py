#! /usr/bin/env python
import sys
from functools import cmp_to_key

def compare(l, k):
    if type(l) is int and type(k) is int:
        if l == k: return 0
        if l < k:  return -1
        return 1
    if type(l) is int:
        return compare([l], k)
    if type(k) is int:
        return compare(l, [k])
    
    # Both are lists
    l = list(l)
    k = list(k)
    while l or k:
        if not l:
            return -1
        if not k:
            return 1
        a, b = l.pop(0), k.pop(0)
        cmp = compare(a, b)
        if cmp != 0:
            return cmp
    return 0

lines = [eval(line.strip()) for line in sys.stdin if line != '\n']
dividers = ([[2]], [[6]])
lines.extend(dividers)

lines.sort(key=cmp_to_key(compare))
lines.insert(0, 0)
print(lines.index([[2]]) * lines.index([[6]]))
