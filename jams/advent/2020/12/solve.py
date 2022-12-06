import sys

x, y = 0, 0
dirs = ['N', 'E', 'S', 'W']
facing = 1

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

for line in sys.stdin:
    line = line.strip()
    command, n = line[0], int(line[1:])
    print(command, n)
    if command == 'L':
        facing -= n // 90
        facing %= 4
    elif command == 'R':
        facing += n // 90
        facing %= 4
    elif command == 'F':
        x, y = move(x, y, dirs[facing], n)
    else:
        x, y = move(x, y, command, n)
    print(x, y)

print(x, y)
print(abs(x) + abs(y))
