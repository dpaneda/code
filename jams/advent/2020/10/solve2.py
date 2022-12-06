import sys

adapters = []

for line in sys.stdin:
    adapters.append(int(line))
adapters.sort()

jolt = 0
jumps = []

for adapter in adapters:
    d = adapter - jolt
    jolt = adapter
    jumps.append(d)
adapters.append(jolt + 3)
jumps.append(3)

def permutations(l):
    if len(l) <= 1:
        return 1
    elif len(l) == 2:
        return 2
    elif len(l) == 3:
        return 4
    elif len(l) == 4:
        return 7

print(jumps)

perm = 1
l = []
for jump in jumps:
    if jump != 3:
        l.append(jump)
    else:
        perm *= permutations(l)
        l = []

print(perm)
