#!/usr/bin/python
import sys

def nextline():
    return sys.stdin.readline().strip()

bindings = int(nextline())
binding = {}

for i in xrange(bindings):
    combo = sorted(nextline().split())
    binding[str(combo)] = nextline()

t = int(nextline())

for i in xrange(t):
    combo = sorted(nextline().split())
    print binding[str(combo)]
