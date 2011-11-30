#!/usr/bin/python

import sys

def solve(n, ei, ai, costs):
    print n, ei, ai
    for i in xrange(n):
        print costs[i]

for line in sys.stdin:
    problem = line.split()
    n = int(problem[0])
    earth_index, atlantis_index = map(int, problem[1:3])
   
    travel = {}
    for i in xrange(n):
        travel[i] = {}
        for j in xrange(n):
            travel[i][j] = -1
    
    for i in problem[3:]:
        a, b, cost = map(int, i.split(','))
        travel[a][b] = cost

    print solve(n, earth_index, atlantis_index, travel)
