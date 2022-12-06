#! /usr/bin/env python
import sys
import collections

polymer = input()
pairs = {}

input()

replaces = {}

for line in sys.stdin:
    pair, new = line.strip().split(' -> ')
    replaces[pair] = new

def decontruct(polymer):
    for i in range(len(polymer) - 1):
        pair = polymer[i:i+2]
        n = pairs.get(pair, 0)
        pairs[pair] = n + 1
    return pairs

def step(pairs):
    new_pairs = {}
    for pair, n in pairs.items():
        if pair not in replaces:
            continue
        p1 = pair[0] + replaces[pair]
        p2 = replaces[pair] + pair[1]
        new_pairs[p1] = new_pairs.get(p1, 0) + n
        new_pairs[p2] = new_pairs.get(p2, 0) + n
    return new_pairs

pairs = decontruct(polymer)
for i in range(40):
    print(pairs)
    pairs = step(pairs)

letters = {}
for pair, n in pairs.items():
    a, b = pair
    letters[a] = letters.get(a, 0) + n / 2
    letters[b] = letters.get(b, 0) + n / 2

print(letters)
print(max(letters.values()) - min(letters.values()) )
