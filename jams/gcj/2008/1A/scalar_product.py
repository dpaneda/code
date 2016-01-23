#!/usr/bin/python
import sys

num = int(sys.stdin.readline())

for case in range(1, num+1):
	size = int(sys.stdin.readline())
	v1 = map(int, sys.stdin.readline().split())
	v2 = map(int, sys.stdin.readline().split())
	v1.sort()
	v2.sort()
	v2.reverse()

	sum = 0
	for i in range(0, size):
		sum += v1[i] * v2[i]
	
	print "Case #%d: %d" % (case, sum)
