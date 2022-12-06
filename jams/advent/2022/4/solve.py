#! /usr/bin/env python
import sys

def full_overlap(a, b):
    def contains(a, b):
        return a[0] <= b[0] and a[1] >= b[1]
    return contains(a, b) or contains(b, a)

def partial_overlap(a, b):
    def overlap_left(a, b):
        return a[0] <= b[0] and a[1] >= b[0]
    return overlap_left(a, b) or overlap_left(b, a)

def parse_pair(line):
    l = line.split(',')
    pair = []
    for elf in l:
        elf = list(map(int, elf.split('-')))
        pair.append(elf)
    return pair

full, partial = 0, 0
for line in sys.stdin:
    a, b = parse_pair(line)
    if full_overlap(a, b):
        full += 1
    if partial_overlap(a, b):
        partial += 1

print(f"Full overlaps: {full}, partial overlap: {partial}")
