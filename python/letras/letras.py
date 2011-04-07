#!/usr/bin/python

import sys,random

for line in sys.stdin:
	palabras = line.split()

	for palabra in palabras:
		reorder = palabra[0]
		if len(palabra) > 3:
			for i in random.sample(palabra[1:-1],len(palabra) - 2):
				reorder += i
		reorder += palabra[-1]
		print reorder,

	print
