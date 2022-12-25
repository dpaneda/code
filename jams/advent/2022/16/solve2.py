#! /usr/bin/env python
import sys
import re
import networkx as nx
import itertools
import random

g = nx.DiGraph()

for line in sys.stdin:
    m = re.search('Valve (.+) has flow rate=(\d+); tunnels? leads? to valves? (.*)', line)
    g.add_node(m[1], rate=int(m[2]))

    for valve in m[3].split(', '):
        g.add_edge(m[1], valve)

def check_solution(g, paths, valves):
    current_valve = 'AA'
    time = 30
    score = 0

    for valve in valves:
        time -= paths[current_valve][valve]
        current_valve = valve
        time -= 1
        if time <= 0:
            return score
        score += time * g.nodes[valve]['rate']
    return score

def check_solution_with_help(g, paths, valves, elephant_valves):
    current_valve = 'AA'
    time = 26
    score = 0

    visited_valves = set()

    for valve in valves:
        time -= paths[current_valve][valve]
        current_valve = valve
        time -= 1
        if time <= 0:
            break
        visited_valves.add(valve)
        score += time * g.nodes[valve]['rate']

    current_valve = 'AA'
    time = 26
    for valve in elephant_valves:
        time -= paths[current_valve][valve]
        current_valve = valve
        if time <= 0:
            break
        if valve in visited_valves:
            # Already opened, no more score
            continue
        time -= 1
        score += time * g.nodes[valve]['rate']

    return score

def mutate(l, k):
    lists = [list(l), list(k)]
    origin_list  = random.randint(0, 1)
    destiny_list = random.randint(0, 1)
    origin_index = random.randint(0, len(lists[origin_list]) - 1)
    destiny_index = random.randint(0, len(lists[destiny_list]) - 1)

    v = lists[origin_list].pop(origin_index)
    lists[destiny_list].insert(destiny_index, v)
    return lists

paths = dict(nx.all_pairs_shortest_path_length(g))
valves = [v for v in g.nodes if g.nodes[v]['rate']]
mid = len(valves) // 2
elephant_valves = valves[mid:]
valves = valves[:mid]

best_score = 0
best_lists = valves, elephant_valves
while True:
    valves, elephant_valves = best_lists
    for _ in range(random.randint(0, 5)):
        valves, elephant_valves = mutate(valves, elephant_valves)

    score = check_solution_with_help(g, paths, valves, elephant_valves)
    if score > best_score:
        print(f"Score {score} for solution {valves} and {elephant_valves}")
        best_score = score
        best_lists = valves, elephant_valves
