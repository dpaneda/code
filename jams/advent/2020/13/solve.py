initial = int(input())
buses = set(input().split(','))
buses.remove('x')
buses = list(map(int, buses))

print(initial, buses)

n = initial
found = False
while not found:
    for bus in buses:
        if n % bus == 0:
            print((n - initial) * bus)
            found = True
    n += 1
