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

def apply_rule_loop(rule, line):
    n = 0
    f = rules[rule]
    while len(line):
        l = f(line[n:])
        if not l:
            break
        n += l.pop()
    return n

matchs = 0
for line in sys.stdin:
    line = line.strip()
    n = apply_rule_loop("42", line)
    n2 = apply_rule_loop("31", line[n:])
    if n > 0 and n2 > 0 and n > n2 and n + n2 == len(line):
        print(line, n, n2)
        matchs += 1
print(matchs)
