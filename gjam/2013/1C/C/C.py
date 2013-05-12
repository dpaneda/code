#!/usr/bin/python2

import sys
import bisect


def calculate_atacks(tribes):
    # We calculate attacks day by day, until no tribe have any attacks left
    attacks = {}
    for tribe in tribes:
        for i in xrange(0, tribe[1]):
            d = tribe[0]
            if d not in attacks:
                attacks[d] = []
            attacks[d].append((tribe[2], tribe[3], tribe[4]))
            # Change tribe status
            tribe[0] += tribe[5]
            tribe[2] += tribe[6]
            tribe[3] += tribe[6]
            tribe[4] += tribe[7]
    return attacks


def raise_wall(wall, wallh, w, e, s):
#    print wall, wallh
#    print w, e, s
    a = bisect.bisect_right(wall, w)
    if a > 0:
        a -= 1
    b = bisect.bisect_right(wall, e)

    print a, b

    insert = False
    if wall[a] < w and wallh[a] < s:
        wall.insert(a + 1, w)
        wallh.insert(a + 1, s)
        b += 1
        insert = True
    elif wall[a] == w and wallh[a] < s:
        wallh[a] = s
        insert = True

    if insert:
        if b >= len(wall):
            wall.insert(a + 2, e)
            wallh.insert(a + 2, 0)
        elif wall[b] > e:
            wall.insert(a + 2, e)
            wallh.insert(a + 2, wall[b])
    for i in xrange(a + 2, b):
        if wallh[i] < s:
            del(wall[i])
            del(wallh[i])
#    print wall, wallh


def wall_minimum_height(wall, wallh, w, e):
    a = bisect.bisect_right(wall, w) - 1
    if a < 0:
        a = 0
    b = bisect.bisect_right(wall, e)
    if a == b:
        return 0
    return min(wallh[a:b])


def succeed(wall, wallh, w, e, s):
    #print w, e, s
    m = wall_minimum_height(wall, wallh, w, e)
    return m < s


def simulate_attacks(attacks):
    wall = [0]
    wallh = [0]
    s = 0
    days = sorted(attacks.iterkeys())
    for day in days:
        for attack in attacks[day]:
            if succeed(wall, wallh, attack[0], attack[1], attack[2]):
                s += 1
        for attack in attacks[day]:
            raise_wall(wall, wallh, attack[0], attack[1], attack[2])
    return s


def Solve():
    ntribes = int(sys.stdin.readline().strip())
    tribes = []
    for i in xrange(0, ntribes):
        d, n, w, e, s, di, pi, si = map(int, sys.stdin.readline().strip().split())
        tribes.append([d, n, w, e, s, di, pi, si])

    attacks = calculate_atacks(tribes)
    return simulate_attacks(attacks)

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s " % (case, Solve())
