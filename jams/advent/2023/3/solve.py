#! /usr/bin/env python

import sys
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Number:
    value: int
    x: int
    y: int
    size: int
    is_part: bool


gears = {}
gear_ratios = 0


def read_number(grid, x, y) -> Number:
    def search_part(x, y) -> bool:
        """Scan for an adjacent symbol"""
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                c = grid[x + dx][y + dy]
                if c == '*':
                    nonlocal gear
                    gear = x + dx, y + dy
                if c != '.' and not c.isdigit():
                    return True
        return False

    size = value = 0
    is_part = False
    gear = None

    while grid[x + size][y].isdigit():
        value *= 10
        value += int(grid[x + size][y])
        if not is_part:
            is_part = search_part(x + size, y)
        size += 1

    global gears, gear_ratios
    if gear in gears:
        gear_ratios += gears[gear] * value
    elif gear:
        gears[gear] = value

    return Number(value, x, y, size, is_part)


# I usually expand the grid one extra slot to avoid dealing with the borders
# but here I used this defaultdict trick instead
grid = defaultdict(lambda: defaultdict(lambda: '.'))
for y, line in enumerate(sys.stdin):
    grid_size = len(line) - 1
    for x, c in enumerate(line.strip()):
        grid[x][y] = c

x, y = 0, 0
numbers = []
while True:
    if grid[x][y].isdigit():
        number = read_number(grid, x, y)
        numbers.append(number)
        x += number.size
    if x > grid_size:
        x, y = 0, y + 1
    else:
        x += 1
    if y > grid_size:
        break

print(sum([n.value for n in numbers if n.is_part]))
print(gear_ratios)
