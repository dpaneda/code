#! /usr/bin/env python

import sys
from collections import Counter
from dataclasses import dataclass
from functools import total_ordering

cards = "0J23456789TQKA"
card_rank = {c: cards.index(c) for c in cards}


@dataclass
@total_ordering
class Hand():
    raw: str
    hand: Counter
    bid: int

    def __init__(self, s):
        s, bid = s.split()
        self.raw = s
        self.hand = Counter(s.replace('J', ''))
        self.bid = int(bid)
        jokers = s.count('J')
        if jokers:
            if s == 'JJJJJ':
                self.hand = Counter(s)
            else:
                top_card = self.hand.most_common()[0][0]
                s = s.replace('J', top_card)
                self.hand = Counter(s)

    def __eq__(self, other):
        return self.hand == other.hand

    def order_counters(self):
        return sorted(self.hand.most_common(),
                      key=lambda x: 1000 * x[1] + card_rank[x[0]],
                      reverse=True)

    def hand_type(self):
        l = [x[1] for x in self.hand.most_common()]
        if l == [5]:
            return 6
        elif l == [4, 1]:
            return 5
        elif l == [3, 2]:
            return 4
        elif l == [3, 1, 1]:
            return 3
        elif l == [2, 2, 1]:
            return 2
        elif l == [2, 1, 1, 1]:
            return 1
        return 0

    def __lt__(self, other):
        if self.hand_type() != other.hand_type():
            return self.hand_type() < other.hand_type()

        for a, b in zip(self.raw, other.raw):
            if card_rank[a] != card_rank[b]:
                return card_rank[a] < card_rank[b]
        return False

        a = self.order_counters()
        b = other.order_counters()

        while a:
            card, _ = a.pop(0)
            card2, _ = b.pop(0)
            rank1, rank2 = card_rank[card], card_rank[card2]
            if rank1 != rank2:
                return rank1 < rank2
        return False


hands = sorted(map(Hand, sys.stdin))
values = [hand.bid * (i + 1) for i, hand in enumerate(hands)]
print(sum(values))
