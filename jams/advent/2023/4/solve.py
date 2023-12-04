#! /usr/bin/env python

import sys
from dataclasses import dataclass
from typing import Set

@dataclass
class Card:
    winners: Set[int]
    owned: Set[int]
    copies: int = 1

    def __init__(self, card_line: str):
        card_line = card_line.split(':')[1]
        numbers = card_line.split('|')
        self.winners, self.owned = map(lambda x: set(map(int, x.split())), numbers)

    def own_winners(self):
        return len(self.winners & self.owned)

    def value(self):
        return int(2 ** (self.own_winners() - 1))


cards = list(map(Card, sys.stdin.readlines()))
points = sum([c.value() for c in cards])
print(f"The total points are {points}")

for i, card in enumerate(cards):
    n = card.own_winners()
    for j in range(i, i+n):       
        if j+1 < len(cards):
            cards[j+1].copies += card.copies

total_cards = sum([c.copies for c in cards])
print(f"The total copies of cards are {total_cards}")
