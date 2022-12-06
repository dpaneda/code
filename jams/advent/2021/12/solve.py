#! /usr/bin/env python
import sys
import networkx as nx
import matplotlib.pyplot as plt

edgelist = map(lambda s: s.strip().replace('-', ' '), sys.stdin.readlines())
G = nx.read_edgelist(edgelist)

#nx.draw_shell(G, with_labels=True)
#plt.show()

open_paths = [["start"]]
closed_paths = []

while open_paths:
    path = open_paths.pop()
    last_node = path[-1]
    for node in G.adj[last_node]:
        print(path, node)
        if node.islower() and node in path:
            continue
        p = list(path)
        p.append(node)
        if node == 'end':
            closed_paths.append(p)
        else:
            open_paths.append(p)

#for path in closed_paths:
#    print(path)
print(len(closed_paths))
