#!/usr/bin/python2

import sys
import numpy as np
import networkx as nx

def generateAllBinaryMatrix(n):
    G = np.zeros([n,n])

    cordx=[]
    cordy=[]
    for x in range(0,n):
        for y in range(0,n):
            cordx.append(x)
            cordy.append(y)

    cx=np.array(cordx)
    cy=np.array(cordy)
    indices=(cx,cy)
    for j in range(0,2**(indices[0].size)):
        G[indices] = [1 if digit=='1' else 0 for digit in bin(j)[2:].zfill(indices[0].size)]
        yield (G)

def solve():
    B, M = map(int, raw_input().split())
    print (B, M)

    # Generate all the fucking solutions
    for m in generateAllBinaryMatrix(5):
        print m
    return ''


num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print("Case #{0}: {1}".format(case, solve()))
