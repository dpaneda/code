#!/usr/bin/python3
import math

def spell_chance(x, y, z, 

def solve():
    n = int(input())
    l = []
    for i in range(n):
        l.append(int(input()))
    trips = 0
    l.sort()
    while l:
        trips += 1
        items = 1
        top = l.pop(-1)
        trip = [top]
        try:
            while items * top < 50:
                items += 1
                trip.append(l.pop(0))
        except IndexError:
            # Not possible to make this trip, items should go in the previous one
            trips -= 1
    return trips

num = int(input())

for case in range(1, num + 1):
    print("Case #%d: %s " % (case, solve()))
