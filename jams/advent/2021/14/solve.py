#! /usr/bin/env python
import sys
import collections

polymer = input()

input()

replaces = {}

for line in sys.stdin:
    pair, new = line.strip().split(' -> ')
    replaces[pair] = new

def step(polymer):
    s = [ polymer[0] ]
    for i in range(1, len(polymer)):
        tip = s[-1] + polymer[i]
        if tip in replaces:
            s += replaces[tip] + polymer[i]
        else:
            s += polymer[i]
    return ''.join(s)

for i in range(40):
    polymer = step(polymer)
    print(i,len(polymer))

    count = collections.Counter(polymer).most_common()
    print(count[0][1])
    #print(count[-1][1])
    #print(count[0][1] - count[-1][1])
