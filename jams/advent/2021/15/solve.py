#! /usr/bin/env python
import sys
import networkx as nx
import matplotlib.pyplot as plt


grid = []
for line in sys.stdin:
    grid.append(list(map(int, line.strip())))

N = len(grid)

G = nx.DiGraph()

def weight(x, y):
    step = x // N + y // N
    x, y = x % N, y % N
    weight = grid[y][x] - 1
    weight = (weight + step) % 9
    weight += 1
    return weight

for x in range(N * 5):
    for y in range(N * 5):
        G.add_edge(f'{x},{y}', f'{x+1},{y}', weight=weight(x + 1, y))
        G.add_edge(f'{x+1},{y}', f'{x},{y}', weight=weight(x, y))
        G.add_edge(f'{x},{y}', f'{x},{y+1}', weight=weight(x, y + 1))
        G.add_edge(f'{x},{y+1}', f'{x},{y}', weight=weight(x, y))

cost = - grid[0][0]
target = (5 * N) - 1
for node in nx.shortest_path(G, '0,0', f'{target},{target}', weight='weight'):
    x, y = map(int, node.split(','))
    n = weight(x, y)
    cost += n
print(cost)
