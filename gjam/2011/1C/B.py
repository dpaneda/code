#!/usr/bin/python
# I think this version does not work... it works on some stage but i broke 
# the implementation while working on improving the algorithm

import sys

def calculate_distance(L, t, N, c, distance, booster):
    actual_distance = 0
    time = 0
    star = 0
    lastparsecs = 0
    parsecs = 0
    while True:
        #print star, time, distance[actual_distance]
        if time >= t and booster[star + 1]:
            coste = 1
        else:
            coste = 2

        recorrido = parsecs - lastparsecs
        falta = distance[actual_distance] - recorrido
        if time >= t or (time + falta * coste) < t:
            time += falta * coste
            parsecs += falta
        else:
            time += coste
            parsecs += 1


        if (parsecs - lastparsecs) == distance[actual_distance]:
            star += 1
            actual_distance = (actual_distance + 1) % len(distance)
            lastparsecs = parsecs
            if star == N:
                break

    return time
 
def Solve():
    l = map(int, sys.stdin.readline().split())
    L = l[0]
    t = l[1]
    N = l[2]
    c = l[3]
    #print L, t, N, c
    distance = []
    for i in range(4, 4 + c):
        distance.append(l[i])
       
    maxdistance = 0
    maxdistance = 0

    for i in range(0, c):
        if distance[i] > distance[maxdistance]:
            maxdistance = i

    #print distance[maxdistance]

    booster = {}
    for i in range(0, N+1):
        booster[i] = False

    if L == 0:
        t = 0

    mintime = calculate_distance(L, t, N, c, distance, booster)
   
    if L == 0:
         return str(mintime)

    if L == 1:
        p = (N / c) 
        if N % c > maxdistance:
            s = (p * c) + maxdistance
        else:
            s = ((p-1) * c) + maxdistance
        print s
        print maxdistance
        booster[s] = True
        time = calculate_distance(L, t, N, c, distance, booster)
        return str(time)

#        for i in range(0, N+1):
#            booster[i] = True
#            time = calculate_distance(L, t, N, c, distance, booster)
#            #print i, time
#            if time < mintime:
#                mintime = time
#            booster[i] = False
#    
#        return str(mintime)

    if L == 2:
        p = (N / c) 
        s = ((p-1) * c) + maxdistance
        s2 = ((p-2) * c) + maxdistance
        booster[s] = True
        booster[s2] = True
        time = calculate_distance(L, t, N, c, distance, booster)
        return str(time)


        for i in range(0, N+1):
            for j in range(0, N+1):
                booster[i] = True
                booster[j] = True
                time = calculate_distance(L, t, N, c, distance, booster)
                if time < mintime:
                    mintime = time
                booster[i] = False
                booster[j] = False
    
    return str(mintime)

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s" % (case, Solve())
