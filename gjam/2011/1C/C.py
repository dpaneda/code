#!/usr/bin/python
# This works well and its clean but not good enought to fight agains large version :)

import sys

def Solve():
    [n, l, h] = map(int,sys.stdin.readline().split())
    notes = map(int,sys.stdin.readline().split())
    index = l
    while index < h+1:
        freq = True
        for i in notes:
            if i % index != 0 and index % i != 0:
                freq = False
                break
        if freq == True:
            return jeff_note
    index += 1
        
    return "NO"

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s" % (case, Solve())
