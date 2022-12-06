import sys
import re
from functools import partial

rules = {}

# Each rule return the number of matches characteres as a set.
# An empty set means no matches
def simple(c, s):
    if s and s[0] == c:
        return {1}
    else:
        return set()
    
def dual(a, b, s):
    f, f2 = rules[a], rules[b]
    l = f(s)
    g = set()
    for n in l:
        temp = f2(s[n:])
        for i in temp:
            g.add(n + i)
    return g

def option(a, b, c, d, s):
    l = dual(a, b, s)
    g = dual(c, d, s)
    return l | g

def simple_option(a, b, s):
    f, g = rules[a], rules[b]
    l, g = f(s), g(s)
    return l | g

def alias(a, s):
    f = rules[a]
    return f(s)

for line in sys.stdin:
    line = line.strip()
    print(line)
    m = re.match('^(\d+): "(\w)"$', line)
    if m:
        n, c = m.groups()
        rules[n] = partial(simple, c)
        continue
    m = re.match('^(\d+): (\d+) (\d+)$', line)
    if m:
        n, a, b = m.groups()
        rules[n] = partial(dual, a, b)
        continue
    m = re.match('^(\d+): (\d+) (\d+) \| (\d+) (\d+)$', line)
    if m:
        n, a, b, c, d = m.groups()
        rules[n] = partial(option, a, b, c, d)
        continue
    m = re.match('^(\d+): (\d+) \| (\d+)$', line)
    if m:
        n, a, b = m.groups()
        rules[n] = partial(simple_option, a, b)
        continue
    m = re.match('^(\d+): (\d+)$', line)
    if m:
        n, a = m.groups()
        rules[n] = partial(alias, a)
        continue
    if not line.strip():
        break

f = rules["0"]
n = 0
for line in sys.stdin:
    line = line.strip()
    l = f(line)
    if len(line) in l:
        print(line)
        n += 1
        continue
    while 24 in l:
        print("JA")
        line = line[23:]
        l = f(line)
        if len(line) in l:
            n += 1

print(n)
