import sys

x, y = 10, -1
ship = 0, 0

def move(x, y, where, n):
    if where == 'N':
        y -= n
    elif where == 'S':
        y += n
    elif where == 'E':
        x += n
    elif where == 'W':
        x -= n
    return x, y

def rotateR(x, y):
    x, y = -y
    x = -y

for line in sys.stdin:
    line = line.strip()
    command, n = line[0], int(line[1:])
    print(command, n)
    if command == 'R':
        for i in range(n // 90):
            x, y = -y, x
    elif command == 'L':
        for i in range(n // 90):
            x, y = y, -x
    elif command == 'F':
        ship = ship[0] + n*x, ship[1] + n*y
    else:
        x, y = move(x, y, command, n)
    print(x, y)
    print(ship)

print(x, y)
print(abs(ship[0]) + abs(ship[1]))
