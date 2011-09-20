#!/usr/bin/python

import sys

n = int(sys.stdin.readline())

for case in xrange(n):
    l = int(sys.stdin.readline())
    t = int(sys.stdin.readline())
    lights = ""

    i = int(not t % 2)

    while i < l and i < t:
        lights += str(i) + " "
        i += 2

    if len(lights):
        print lights.strip()
    else:
        print  "All lights are off :("
