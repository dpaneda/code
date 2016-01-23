#!/usr/bin/python

import sys

def Solve():
    out = ""
    [r, c] = map(int,sys.stdin.readline().split())
    tiles = []
    for i in range(0, r):
        tiles.append(list(sys.stdin.readline().strip()))

    for i in range(0, r):
        for j in range(0, c):
            try:
                if tiles[i][j] == '#' and tiles[i][j+1] == '#'     and tiles[i+1][j] == '#'     and tiles[i+1][j+1] == '#':
                    tiles[i][j] = '/'
                    tiles[i][j+1] = '\\'
                    tiles[i+1][j] = '\\'
                    tiles[i+1][j+1] = '/'
            except:
                pass
    
    for i in range(0, r):
        out += '\n' 
        for j in range(0, c):        
            out += tiles[i][j]
        
    imposible = False
    for i in range(0, r):
        for j in range(0, c):        
            if tiles[i][j] == '#':
                imposible = True
    if imposible:
        out = "\nImpossible"

    return out

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s" % (case, Solve())
