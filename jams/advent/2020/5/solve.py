import sys

l = set()
for line in sys.stdin:
    line = line.strip().replace('B', '1').replace('F', '0').replace('L', '0').replace('R', '1')
    l.add(int(line, 2))

for i in range(1, max(l)):
    if i not in l:
        if i-1 in l and i+1 in l:
            print(i)
print(max(l))
