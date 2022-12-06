import sys

positions = None
for line in sys.stdin:
    l = list(line.strip())
    if not positions:
        positions = list(map(list, l))
    else:
        for i in range(len(l)):
            positions[i].append(l[i])

gamma = ""
epsilon = ""

for l in positions:
    if l.count("1") > l.count("0"):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(positions, gamma, epsilon)

a = int(gamma, 2)
b = int(epsilon, 2)
print(a * b)
