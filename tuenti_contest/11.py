#!/usr/bin/python

from tuenti import *

def solve(k, df, n, stations):
    fuel = k
    stops = ""
    last = 0
    for gas in xrange(n):
        fuel -= stations[gas] - last
        last = stations[gas]
        if gas < n - 1 and fuel < (stations[gas + 1] - stations[gas]):
            stops = stops + str(stations[gas]) + " "
            fuel = k
    if stops:
        return str(stops).strip()
    else:
        return "No stops"

n = int_read()

for case in xrange(n):
    k, d, f = int_read(), int_read(), int_read()
    stations = int_list_read()
    print solve(k, d, f, stations)
