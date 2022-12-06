import sys

l = []
for line in sys.stdin:
    l.append(int(line))

c = 0
for i in range(1, len(l)-2):
    a = sum(l[i-1:i+2])
    b = sum(l[i:i+3])
    if b > a:
        c+= 1
print(c)
