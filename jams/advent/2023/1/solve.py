#! /usr/bin/env python
import sys

def numbers_replace(s):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i, name in enumerate(numbers):
        s = s.replace(name, f"{name}{i}{name}")
    return s

n = 0
for line in map(numbers_replace, sys.stdin):
    numbers = [i for i in line if i.isdigit()]
    a = int(numbers[0]) * 10 + int(numbers[-1])
    n += a
print(n)
