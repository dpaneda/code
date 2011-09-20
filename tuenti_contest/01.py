#!/usr/bin/python

import sys

for line in sys.stdin:
    numbers = map(long, line.split())
    print reduce(lambda x, y: x + y, numbers)
