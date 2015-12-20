#!/usr/bin/python2

import sys


def insert_times(n, delay, a, b):
    """Insert times of arrival and departures in minutes

       Reads n lines from standard input, convert is to minutes
       and insert them in the station hash (a or b)
    """
    for i in xrange(0, n):
        line = sys.stdin.readline().strip()
        dep, arr = line.split()
        dephour, depmin = map(int, dep.split(':'))
        arrhour, arrmin = map(int, arr.split(':'))
        deptotal = dephour * 60 + depmin
        arrtotal = arrhour * 60 + arrmin + delay
        if deptotal not in a:
            a[deptotal] = []
        if arrtotal not in b:
            b[arrtotal] = []
        a[deptotal].append(-1)
        b[arrtotal].append(1)


def simulate(trains):
    needed = 0
    actual = 0
    sortedtimes = sorted(trains.iterkeys())
    for time in sortedtimes:
        for v in trains[time]:
            actual += v
        if actual < 0:
            needed -= actual
            actual = 0
    return needed


def Solve():
    delay = int(sys.stdin.readline())
    na, nb = map(int, sys.stdin.readline().split())
    a_trains = {}
    b_trains = {}
    insert_times(na, delay, a_trains, b_trains)
    insert_times(nb, delay, b_trains, a_trains)

    return str(simulate(a_trains)) + " " + str(simulate(b_trains))


num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s" % (case, Solve())
