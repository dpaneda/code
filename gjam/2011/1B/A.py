#!/usr/bin/python

import sys
from copy import deepcopy

def get_wp(team, results):
    wins = losses = 0.0
    for i in results[team]:
        if i == '1':
            wins += 1
        if i == '0':
            losses += 1
   # print wins
    #print losses
    return wins / (wins + losses)

def Solve():
    teams = int(sys.stdin.readline())
    results = {}
    wp = {}
    rpi = {}
    owp = {}
    oowp = {}
    for team in range(0, teams):
        results[team] = sys.stdin.readline().strip()
        #print results[team]

    for team in results:
        wp[team] = get_wp(team, results)
           
    for team in results:
        _owp = size = 0.0
        results_noteam = deepcopy(results)
        #print results_noteam
        for r in results_noteam:
            #print results_noteam[r]
            results_noteam[r] = results_noteam[r][:team] + '.' + results_noteam[r][team+1:]
            #print "kkkk" +  results_noteam[r]
    
        _owp = size = 0.0
        for i in range(0, len(results[team])):
            #print "---" +  results[team]
            #print "[" + results[team][i] + "]"
            if results[team][i] != '.':
                _owp += get_wp(i, results_noteam)
                size += 1
        owp[team] = _owp / size
    
    for team in results:
        _oowp = size = 0.0
        for i in range(0, len(results[team])):
            if results[team][i] != '.':
                _oowp += owp[i]
                size += 1
        oowp[team] = _oowp / size
 
    for team in results:
        rpi[team] = 0.25 * wp[team] + 0.5 * owp[team] + 0.25 * oowp[team]
        #print wp[team]
        #print owp[team]
        #print oowp[team]
        print rpi[team]
    
num = int(sys.stdin.readline())

for case in range(1, num + 1):
    #sys.stdin.readline() # skip
    print "Case #%d:" % case
    Solve()
