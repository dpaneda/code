#!/usr/bin/python2

import sys
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

def shortest_path(grid, start, end):
    def get_neighbors(p):
        neig = [Point(p.x, p.y - 1),
                Point(p.x, p.y + 1),
                Point(p.x - 1, p.y),
                Point(p.x + 1, p.y)]
        return neig

    def free_neighbors(p):
        good_neig = []
        for neig in get_neighbors(p):
            try:
                if p.x >= 0 and p.y >= 0 and grid[p.x][p.y] == 0:
                    good_neig.append(neig)
            except:
                pass
        return good_neig

    explored = {start}
    border = {start}
    paths = {start: []}

    while border:
        ps = list(border)
        explored |= border
        border = set()

        for p in ps:
            for neig in free_neighbors(p):
                where, n = neig
                if neig not in explored:
                    paths[neig] = paths[p] + [neig]
                    border.add(neig)
                    if neig == end:
                        return paths[neig]
    return None

def get_distance(distances, a, b):
    if a < b:
        return distances[a][b]
    else:
        return distances[b][a]

def get_distances(grid, mices):
    distances = {}
    n = len(mices)
    for i in xrange(n):
        distances[i] = {}
        for j in xrange(i + 1, n):
            path = shortest_path(grid, mices[i], mices[j])
            if path:
                distances[i][j] = len(path)
            else:
                distances[i][j] = 999999999
    return distances
    
best_cost = 9999999

def solve(mices, distances, last, unexplored, cost):
    global best_cost 

    if cost >= best_cost:
        return 999999

    if not unexplored:
        if cost < best_cost:
            best_cost = cost
        return cost

    if len(unexplored) == 1:
        cost += get_distance(distances, last, unexplored[0])
        if cost < best_cost:
            best_cost = cost
        return cost
        
    minimum = 999999
    for i in unexplored:
        l = list(unexplored)
        l.remove(i)
        c = solve(mices, distances, i, l, cost + get_distance(distances, last, i))
        if c < minimum:
            minimum = c
    return minimum

cases = int(raw_input())

for case in xrange(cases):
    S = int(raw_input())
    m, n = map(int, raw_input().split())

    grid = []
    mices = []
    start = None

    for i in xrange(n):
        line = raw_input().replace(' ','').strip()
        for j in xrange(m):
            if line[j] == 'M':
                mices.append(Point(i, j))
            if line[j] == 'B':
                start = Point(i, j)

        row = map(int, list(line.replace('X','1').replace('O','0').replace('M','0').replace('B','0')))
        grid.append(row)

    mices.insert(0, start)
    distances = get_distances(grid, mices)
    best_cost = 999999
    d = solve(mices, distances, 0, range(1, len(mices)), 0)
    if d > S:
        print 'NO'
    else:
        print S - d
