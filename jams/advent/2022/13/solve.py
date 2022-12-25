#! /usr/bin/env python
import sys

def compare(l, k):
    l = list(l)
    k = list(k)
    if type(l) is int or type(k) is int:
        if type(l) == type(k):
            if l == k:
                return None
            return l < k
        if type(l) is int:
            return compare([l], k)
        if type(k) is int:
            return compare(l, [k])
    # Both are lists
    while l or k:
        if not l and not k:
            return False
        if not l:
            return True
        if not k:
            return False
        a, b = l.pop(0), k.pop(0)
        cmp = compare(a, b)
        if cmp is not None:
            return cmp
    return None

index = 1
result = 0

lines = sys.stdin.readlines()

while lines:
    l = eval(lines.pop(0))
    k = eval(lines.pop(0))
    if lines:
        lines.pop(0)
    if compare(l, k):
        result += index
        print(f"+ {index}")
    index += 1

print(result)
