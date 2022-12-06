import sys

l = []
for line in sys.stdin:
    a, b = line.split()
    l.append((a, int(b)))

xpos, ypos = 0, 0
while l:
    a, b = l.pop(0)
    if a == 'forward':
        xpos += b
    elif a == 'down':
        ypos += b
    elif a == 'up':
        ypos -= b

    ypos = max(0, ypos)
print(xpos * ypos)
