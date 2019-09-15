#!/usr/bin/python2


R = set('R')
P = set('P')
S = set('S')
RP = set(['R', 'P'])
RS = set(['R', 'S'])
PS = set(['P', 'S'])

found = False

def get_movements(robots, n):
    movements = set()
    for r in robots:
        movements.add(r[n % len(r)])
    return movements

def options(movement):
    if movement == R:
        return RP
    elif movement == P:
        return PS
    elif movement == S:
        return RS
    elif movement == RP:
        return P
    elif movement == RS:
        return R
    elif movement == PS:
        return S
    else:
        return None

def filter_robots(robots, move, n):
    if move == 'R':
        return filter(lambda r: r[n % len(r)] != 'S', robots)
    if move == 'P':
        return filter(lambda r: r[n % len(r)] != 'R', robots)
    if move == 'S':
        return filter(lambda r: r[n % len(r)] != 'P', robots)

def go(robots, n):
    ops = options(get_movements(robots, n))
    if not ops:
        return None

    # Quick check for the win
    for m in ops:
        if not filter_robots(robots, m, n):
            return m

    # Need to go deeper
    for m in ops:
        nr = filter_robots(robots, m, n)
        movs = go(nr, n + 1)
        if movs != None:
            return m + movs    

def solve():
    A = input()
    robots = []
    n = 0
    for i in xrange(A):
        robots.append(raw_input())

    robots = set(robots)
    movements = go(robots, 0)
    if not movements:
        return "IMPOSSIBLE"
    else:
        return movements

cases = input()
for case in xrange(1, cases + 1):
    print "Case #{}: {}".format(case, solve())
