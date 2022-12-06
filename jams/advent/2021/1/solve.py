import sys

l = []
for line in sys.stdin:
    l.append(int(line))

last = l.pop(0)
c = 0
while l:
    n = l.pop(0)
    if n > last:
        c += 1
    last = n
print(c)
