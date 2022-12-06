#! /usr/bin/env python
import sys
import networkx as nx
from dataclasses import dataclass
from typing import List

edgelist = map(lambda s: s.strip().replace('-', ' '), sys.stdin.readlines())
G = nx.read_edgelist(edgelist)

@dataclass
class Path:
    path : List[str]
    revisited : bool = False

open_paths = [ Path(["start"]) ]
closed_paths = []

while open_paths:
    path = open_paths.pop()
    last_node = path.path[-1]
    for node in G.adj[last_node]:
        if node == 'start':
            continue
        revisited = path.revisited
        if node.islower() and node in path.path:
            if revisited:
                continue
            else:
                revisited = True
        p = list(path.path)
        p.append(node)
        new_path = Path(p, revisited)
        if node == 'end':
            closed_paths.append(new_path)
        else:
            open_paths.append(new_path)

print(len(closed_paths))
