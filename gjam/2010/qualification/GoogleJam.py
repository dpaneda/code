#!/usr/bin/python
import sys

class GoogleJam:
	def __init__(self, ResolveCase):
		num = int(sys.stdin.readline())

		for i in range(1, num+1):
			line = sys.stdin.readline().split()
			print "Case #%d: %s" % (i, ResolveCase(line))
