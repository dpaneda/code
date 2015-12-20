#!/usr/bin/env python2

import sys

keymap = {
    'a': 2,
    'b': 22,
    'c': 222,
    'd': 3,
    'e': 33,
    'f': 333,
    'g': 4,
    'h': 44,
    'i': 444,
    'j': 5,
    'k': 55,
    'l': 555,
    'm': 6,
    'n': 66,
    'o': 666,
    'p': 7,
    'q': 77,
    'r': 777,
    's': 7777,
    't': 8,
    'u': 88,
    'v': 888,
    'w': 9,
    'x': 99,
    'y': 999,
    'z': 9999,
    ' ': 0,
}


def resolve():
    line = sys.stdin.readline().strip('\n')
    cad = ''
    for c in line:
        if cad and int(cad[-1]) == keymap[c] % 10:
            cad += ' '
        cad += str(keymap[c])
    return cad

num = int(sys.stdin.readline())

for i in range(1, 1 + num):
    print "Case #%d: %s" % (i, resolve())
