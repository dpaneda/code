import sys

l = []
for line in sys.stdin:
    a, b = line.split()
    l.append((a, int(b)))

aim, xpos, ypos = 0, 0, 0
while l:
    a, b = l.pop(0)
    if a == 'forward':
        xpos += b
        ypos += aim * b
    elif a == 'down':
        aim += b
    elif a == 'up':
        aim -= b

    ypos = max(0, ypos)
print(xpos * ypos)
