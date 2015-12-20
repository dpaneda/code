#!/usr/bin/python2

# Disclaimer: The submit input seems a little broken, like a corrupted
# base64, but it seems to be crafted that way on purpose... not cool imho

import re
import sys

lines = sys.stdin.readlines()

while True:
    if not lines:
        sys.exit(0)

    s = lines.pop(0).strip()
    to_match = lines.pop(0).strip()

    s2 = ""
    groups = []
    group = ""
    negate_mode = False

    for c in s:
        if negate_mode:
            if c == '!':
                s2 += ')'
                negate_mode = False
                groups.append(group)
                group = ""
            else:
                group += c
        else:
            if c == '!':
                s2 += '(*'
                negate_mode = True
            else:
                s2 += c

    s2 = '^' + s2.replace('^', '[A-Z]').replace('?','.').replace('*', '.*') + '$'

    r = re.compile(s2)
    m = r.match(to_match)

    if m:
        bad = False
        for i in xrange(len(groups)):
            if groups[i] in m.group(i + 1):
                bad = True
        if bad:
            print 'n'
        else:
            print 'y'
    else:
        print 'n'
