#!/usr/bin/python

import sys
import re

def resolve(expr):
    if not expr:
        return 0

    if expr.isdigit():
        return int(expr)

    subexpr = "(\d+|\^.*\$)"
    fullexpr = "\^([=#@]) ?%s? %s\$" % (subexpr, subexpr)
    m = re.search(fullexpr, expr)
    op, a, b = m.groups()
    ra, rb = resolve(a), resolve(b)

    if (op == '='):
        return ra + rb
    elif (op == '#'):
        return ra * rb
    else:
        return ra - rb

for line in sys.stdin:
    print resolve(line)
