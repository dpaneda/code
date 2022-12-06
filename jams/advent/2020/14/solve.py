import sys
import re

mem = {}
for line in sys.stdin:
    m = re.search('mask = ([0X1]+)', line)
    if m:
        s = m.group(1)
        andmask = int(s.replace('X','1'), 2)
        ormask = int(s.replace('X','0'), 2)
        continue
    m = re.search('mem\[(\d+)\] = (\d+)', line)
    if m:
        a, b = map(int, (m.group(1), m.group(2)))
        b &= andmask
        b |= ormask
        mem[a] = b
print(sum(mem.values()))
