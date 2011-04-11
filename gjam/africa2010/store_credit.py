#!/usr/bin/python

import sys


def resolve(credit, items, len):
	#len = len(list)
	for i in range(0, len):
		for j in range(i+1, len):
			sum = int(items[i]) + int(items[j])
			if sum == credit:
				return "%d %d" %(i+1, j+1)

num = int(sys.stdin.readline())

for i in range(0, num):
	credit = int(sys.stdin.readline())
	len = int(sys.stdin.readline())
	items = sys.stdin.readline().split()
	choosen = resolve(credit, items, len)
	print "Case #%d: %s" % (i+1, choosen)
	

