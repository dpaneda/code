#! /usr/bin/env python

import re, sys
from collections import defaultdict

stacks = defaultdict(list) 
for line in sys.stdin:
    if '1' in line:
        input()
        break
    for i in range(0, len(line) // 4):
        index = 1 + 4*i
        if line[index] != ' ':
            stacks[i+1].insert(0, line[index])

print(stacks)

for line in sys.stdin:
    m = re.search('move (\d+) from (\d+) to (\d+)', line)
    count, origin, destiny = map(int, m.groups())
    stacks[destiny] += stacks[origin][-count:]
    stacks[origin] = stacks[origin][:-count]

tops = ''.join([stacks[str(i)].pop() for i in range(len(stacks))])
print(tops)
