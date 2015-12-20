#!/usr/bin/python2

import sys

n = int(sys.stdin.readline())
seqs = {}

original = []

for i in xrange(0, n):
    seq = map(int, sys.stdin.readline().split())
    seqs[i] = seq[1:]

selected = -1

while True:
    m = 10 ** 6 + 1
    for i in xrange(0, n):
        if not seqs[i]:
            continue
        if seqs[i][0] < m:
            selected = i
            m = seqs[i][0]
    if m <= 10 ** 6:
        original.append(m)
        seqs[selected] = seqs[selected][1:]
    else:
        break

last = None
for i in original:
    if i != last:
        last = i
        print i,
