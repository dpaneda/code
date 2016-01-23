#!/usr/bin/python
# This one was near.. but don't work... dammit!

import sys

#def get_room_size(begin, end, n):
    

def Solve():
    [n, m] = map(int, sys.stdin.readline().split())
    begin = map(int, sys.stdin.readline().split())
    end = map(int, sys.stdin.readline().split())
        
    mind = 9999999

    for wall in range(0, m):
        begin[wall] -= 1
        end[wall] -= 1

    #print n, m
    #print begin
    #print end

    for wall in range(0, m):
        d1 = abs(end[wall] - begin[wall])
        d2 = abs((end[wall] - n)- begin[wall])
        #print d1
        #print d2
        if d1 < d2:
            d = d1
        else:
            d = d2
        if d < mind:
            mind = d
    #print mind
    ncolors = mind + 1 
    #print ncolors
    
    color = {}

    for v in range(0, n):
        color[v] = None

    c = 0
    change = True
    v = begin[0]
    while color[v] == None:
        for wall in range(0, m):
            if begin[wall] == v or end[wall] == v:
                if change:
                    c = 0
                change = not change

        color[v] = c + 1

        print v, c
        c = (c + 1) % ncolors
        v = (v + 1) % n
        
#    for v in range(0, n):
#        b = (v + 1) % n
#        a = (v + n - 1) % n
#        change = False
#        for wall in range(0, m):
#            o = None
#            if begin[wall] == v:
#                beginwall = not beginwall
#                change = True
#            if end[wall] == v:
#                beginwall = not beginwall
#                change = True
#
#        c += 1
#        color[v] = c
#        if change:
#            c = 0
#
#       if    
#        if color[b] != None:
#            try:
#                colors.remove(color[b])
#            except:
#               pass
#
#        if color[a] != None:
#            try:
#                colors.remove(color[a])
#            except:
#                pass
#
#        for wall in range(0, m):
#            o = None
#            if begin[wall] == v:
#                o = end[wall]
#            if end[wall] == v:
#                o = begin[wall]
#
#            if o != None and color[o] != None:
#                try:
#                    colors.remove(color[o])
#                except:
#                    pass

#        color[v] = colors[0]

    colores = str(ncolors)
    colores += "\n"
    for i in color:
        colores += str(color[i]) + " "
   
     
    return colores

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s" % (case, Solve())
