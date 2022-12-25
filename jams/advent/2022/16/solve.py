#! /usr/bin/env python
import sys
import re
import networkx as nx
import matplotlib.pyplot as plt
import itertools

g = nx.DiGraph()

for line in sys.stdin:
    m = re.search('Valve (.+) has flow rate=(\d+); tunnels? leads? to valves? (.*)', line)
    g.add_node(m[1], rate=int(m[2]))

    for valve in m[3].split(', '):
        g.add_edge(m[1], valve)

def get_distances(g):
    """Calculate the distances between all non-broken valves"""
    pass


def check_solution(g, paths, valves):
    current_valve = 'AA'
    time = 30
    score = 0

    for valve in valves:
        if current_valve:
            time -= paths[current_valve][valve]
            current_valve = valve
        time -= 1
        if time <= 0:
            return score
        score += time * g.nodes[valve]['rate']
    return score


paths = dict(nx.all_pairs_shortest_path_length(g))
valves = [v for v in g.nodes if g.nodes[v]['rate']]
solution = valves

best_score = 0
for solution in itertools.permutations(solution):
    score = check_solution(g, paths, solution)
    if score > best_score:
        print(f"Score {score} for solution {solution}")
        best_score = score
