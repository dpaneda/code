#!/usr/bin/python
# Obviusly a work in progress

import sys

def finish(words, n):
	s = sum(map(len, words.itervalues()))
	return s <= n

def count(words, n):
	ret = {}
	for i in xrange(0, n):
		if not words[i]:
			continue
		c = words[i][0]	
		if c not in ret:
			ret[c] = 0
		ret[c] += 1
	return ret 

def popall(words, n):
	for i in xrange(0, n):
		if words[i]:
			words[i].pop(0)


def can_fix(word, last, candidate):
	if last == candidate:
		return True
	try:
		if last == word[0] and word[1] == candidate:
			return True
	except KeyError:
		return False
	return False

def fix(word, last, candidate):
	if last == candidate:
		word.insert(0, candidate)
		return True
	if last == word[0] and word[1] == candidate:
		word.pop(0)
		return True

def fix_all(words, last, candidate, n):
	s = 0
	for i in xrange(0, n):
		if words[i] and words[i][0] == candidate:
			continue
		if not can_fix(words[i], last[i], candidate):
			return -1

	for i in xrange(0, n):
		if words[i] and words[i][0] == candidate:
			continue
		fix(words[i], last[i], candidate)
		s += 1
	return s

def set_last(words, last, n):
	for i in xrange(0, n):
		last[i] = words[i][0]

def solve():
	n = int(sys.stdin.readline())
	words = {}
	last = {}
	for i in xrange(0, n):
		words[i] = list(sys.stdin.readline().strip()) + [0]
		last[i] = None

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
