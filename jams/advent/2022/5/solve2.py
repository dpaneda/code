#! /usr/bin/env python

import re, sys
from collections import defaultdict

raw_stack = []
line = input()
while '1' not in line:
    raw_stack.append(line)
    line = input()

n = list(map(int, line.split())).pop()
stacks = defaultdict(list) 
while raw_stack:
    row = raw_stack.pop()
    for i in range(0, n):
        index = 1 + 4*i
        if len(row) > index and row[index] != ' ':
            stacks[i+1].append(row[index])

input() # skip

for line in sys.stdin:
    m = re.search('move (\d+) from (\d+) to (\d+)', line)
    count, origin, destiny = map(int, m.groups())
    stacks[destiny] += stacks[origin][-count:]
    stacks[origin] = stacks[origin][:-count]

tops = ''.join([v.pop() for v in stacks.values()])
print(tops)
