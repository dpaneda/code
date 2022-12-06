import sys

adapters = []

for line in sys.stdin:
    adapters.append(int(line))
adapters.sort()

jolt = 0
jumps = [0] * 4

for adapter in adapters:
    d = adapter - jolt
    jumps[d] += 1
    jolt = adapter
jumps[3] += 1

print(jumps[1] * jumps[3])
