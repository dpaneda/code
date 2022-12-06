import sys
import copy

n = 94
seats = [['.'] * (n+2)]

for line in sys.stdin:
    line = f'.{line.strip()}.'
    seats.append(list(line))
seats.append(['.'] * (n+2))

def print_seats(seats):
    for l in seats:
        print("".join(l))

def empty_seats(seats, a, b):
    count = 0
    for y in range(b-1, b+2):
        for x in range(a-1, a+2):
            if (a, b) == (x, y):
                continue
            if seats[y][x] == '#':
                count += 1
    return count

def iterate(seats):
    change = False
    seats2 = copy.deepcopy(seats)
    for y in range(1, len(seats)):
        for x in range(1, len(seats[0])):
            if seats[y][x] == '.':
                continue
            free = empty_seats(seats, x, y)
            if free == 0 and seats[y][x] == 'L':
                seats2[y][x] = '#'
                change = True
            elif free >=4 and seats[y][x] == '#':
                seats2[y][x] = 'L'
                change = True
    return seats2, change

def count_seats(seats):
    count = 0
    for l in seats:
        count += l.count('#')
    return count

def free_map(seats):
    seats2 = copy.deepcopy(seats)
    for x in range(1, n+1):
        for y in range(1, n+1):
            if seats[y][x] == '.':
                continue
            free = empty_seats(seats, x, y)
            seats2[y][x] = str(free)
            continue
            if free == 0:
                seats2[y][x] = '#'
            elif free >=4:
                seats2[y][x] = 'L'
    return seats2

change = True
while change:
    seats, change = iterate(seats)
    print(count_seats(seats))
print_seats(seats)
print(count_seats(seats))
