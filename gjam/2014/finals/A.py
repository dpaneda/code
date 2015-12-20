#!/usr/bin/python

import sys

class Matrix:
    m = {}
    rmap = {}
    cmap = {}

    def get(r, c):
    def


def solve():
	n = int(sys.stdin.readline())
	m = {}
	for i in xrange(0, n):
		m[i] = list(sys.stdin.readline().strip())

	i = 0
	removed = 0
	while not finish(words, n):
		c = count(words, n)
		while c:
			candidate = max(c, key=c.get)
			r = fix_all(words, last, candidate, n)
			if r == -1:
				if len(c) > 1:
					del(c[candidate])
					continue
				else:
					return "Fegla Won"
			removed += r
			set_last(words, last, n)
			popall(words, n)
			break

	return str(removed)

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s" % (case, solve())
