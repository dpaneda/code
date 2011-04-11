#!/usr/bin/python

import sys

num = int(sys.stdin.readline())

for i in range(0, num):
	words = sys.stdin.readline().split()
	rline = ""
	for word in reversed(words):
		if len(rline) > 0:
			rline += " "
		rline += str(word)
	
	print "Case #%d: %s" % (i+1, rline)
