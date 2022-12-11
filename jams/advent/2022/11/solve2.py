#! /usr/bin/env python
from dataclasses import dataclass
from typing import List, Tuple
import operator
import re
import sys

ROUNDS = 10000

@dataclass()
class Monkey:
    mid: int
    items: List[int]
    operation: str
    test_number: int
    destinations: Tuple[int, int]
    inspections: int = 0

    def parse() -> 'Monkey':
        number = r'(\d+)'
        m = re.search(f'Monkey {number}:', input())
        mid = int(m[1])
        m = re.search('Starting items: (.*)', input())
        items = list(map(int, m[1].split(',')))
        m = re.search('Operation: new = (.*)', input())
        operation = m[1]
        m = re.search(f'Test: divisible by {number}', input())
        test_number = int(m[1])
        m = re.search(f'If true: throw to monkey {number}', input())
        m2 = re.search(f'If false: throw to monkey {number}', input())
        destinations = (int(m[1]), int(m2[1]))
        return Monkey(mid, items, operation, test_number, destinations)

    def inspect(self, monkeys):
        while self.items:
            old = self.items.pop(0)
            new = eval(self.operation)
            new = new % 9699690 # Sorry about this xD
            if new % self.test_number == 0:
                target = self.destinations[0]
            else:
                target = self.destinations[1]
            self.inspections += 1
            monkeys[target].items.append(new)


monkeys = []
while True:
    monkeys.append(Monkey.parse())
    if not sys.stdin.readline():
        break

for r in range(ROUNDS):
    [m.inspect(monkeys) for m in monkeys]

monkeys.sort(key=operator.attrgetter("inspections"), reverse=True)

print(monkeys[0].inspections * monkeys[1].inspections)
