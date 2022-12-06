import sys
import re
from functools import partial

def between(a, b, n):
    return a <= n <= b

rules = {}
tickets = []
fields = {}

for line in sys.stdin:
    m = re.match("([^:]+): (\d+)-(\d+) or (\d+)-(\d+)", line)
    if not m:
        break
    name = m.group(1)
    a, b, c, d = map(int, m.groups()[1:])
    rules[name] = (partial(between, a, b), partial(between, c, d))

for line in sys.stdin:
    if ',' in line:
        l = list(map(int, line.split(',')))
        tickets.append(l)

for rule in rules:
    fields[rule] = set(range(len(tickets[0])))

def valid_ticket(ticket):
    for n in ticket:
        valid = False
        for rule in rules.values():
            r1, r2 = rule
            if r1(n) or r2(n):
                valid = True
        if not valid:
            return False
    return True

def process_ticket(ticket, fields):
    for i in range(len(ticket)):
        n = ticket[i]
        for rule, (r1, r2) in rules.items():
            if not (r1(n) or r2(n)):
                fields[rule].discard(i)

for ticket in tickets:
    if valid_ticket(ticket):
        process_ticket(ticket, fields)

for i in range(len(fields)):
    for field, l in fields.items():
        if len(l) == 1:
            n = l.pop()
            for field in fields:
                fields[field].discard(n)
            l.add(n)

n = 1
for field, l in fields.items():
    if field.startswith('departure'):
        i = l.pop()
        n *= tickets[0][i]
print(n)
