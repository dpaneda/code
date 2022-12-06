import sys
import re

mem = {}
for line in sys.stdin:
    m = re.search('mask = ([0X1]+)', line)
    if m:
        targets = ['']
        mask = m.group(1)
    m = re.search('mem\[(\d+)\] = (\d+)', line)
    if m:
        a, b = map(int, (m.group(1), m.group(2)))
        targets = ['']
        for i in range(len(mask)):
            c = mask[i]
            nt = set()
            if c == 'X':
                for t in targets:
                    nt.add(f'{t}0')
                    nt.add(f'{t}1')
            elif c == '0':
                for t in targets:
                    n = 1 << (35 - i) & a
                    if n:
                        nt.add(f'{t}1')
                    else:
                        nt.add(f'{t}0')
            elif c == '1':
                for t in targets:
                    nt.add(f'{t}1')
            targets = nt
        #for target in targets:
        #    print(target)
        targets = [int(t, 2) for t in targets]
        for target in targets:
            mem[target] = b
        #print(mem)
print(sum(mem.values()))
