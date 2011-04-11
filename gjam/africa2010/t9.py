#!/usr/bin/python

import sys

num = int(sys.stdin.readline())

keys = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

def find(f, seq):
	for key in range(0, len(seq)):
		p = seq[key].rfind(f)
		pul = ""
		if p >= 0:
			for i in range(-1,p):
				pul += str(key)
			return pul

oldpress = ""
for i in range(0, num):
	line = sys.stdin.readline()
	outline = "Case #%d: " % (i+1)
	for c in line:
		press = find(c, keys)
		if not press or len(press) < 1:
			continue
		if press[0] == outline[-1]:
			outline += " "
		outline += press
	print outline
