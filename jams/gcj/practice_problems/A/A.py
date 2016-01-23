#!/usr/bin/python

import sys
import math
import pdb

num = int(sys.stdin.readline())

for numcase in range(1, num+1):
	case = sys.stdin.readline().split()
	source_number = case[0]

	s,t = {},{}
	pos = 0
	for i in case[1]:
		s[i] = pos
		pos += 1
	s["base"] = pos

	pos = 0
	for i in case[2]:
		t[pos] = i
		pos += 1
	t["base"] = pos

	pos = number = 0
	while pos < len(source_number):
		number *= s["base"]
		number += s[source_number[pos]]
		pos += 1

	target_number = ""
	while number > 0:
		rest = number % t["base"]
		target_number = t[rest] + target_number
		number /= t["base"]

	print "Case #%d: %s" % (numcase, target_number)
