import sys

vertex = {}

for line in sys.stdin:
    data = line.split(" ")
    target = f"{data[0]} {data[1]}"
    data = data[5:]
    while len(data) > 2:
        origin = f"{data[0]} {data[1]}"
        if origin not in vertex:
            vertex[origin] = set()
        vertex[origin].add(target)
        data = data[4:]

print(vertex)

explored = set()
edge = {'shiny gold'}

while edge:
    new_edge = set()
    for v in edge:
        if v in explored:
            continue
        if v in vertex:
            for v2 in vertex[v]:
                new_edge.add(v2)
        explored.add(v)
    edge = new_edge

print(len(explored) - 1)
