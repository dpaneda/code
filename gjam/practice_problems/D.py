#!/usr/bin/python

import sys

class Item(object):
    def __init__(self, name, x, y, price):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.price = int(price)
        self.perish = (name[-1] == '!')

def Solve():
    [nitems, nstores, gasprice] = map(int, sys.stdin.readline().split())
    req_items = sys.stdin.readline().split()
    items = []
    index = 0
    while index < nstores:
        line = sys.stdin.readline().split()
        (x, y)  = (line[0], line[1])
        line = line[2:]
        for product in line:
            [item, price] = product.split(':')
            items.append(Item(item, x, y, price))
        index += 1

    print req_items
    for i in items:
        print "%s [%d, %d] : %d %s" % (i.name, i.x, i.y, i.price, i.perish)

    return "NO"

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s" % (case, Solve())
