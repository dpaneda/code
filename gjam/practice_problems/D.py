#!/usr/bin/python
# Don't event pass the small set, bugs ahead!


import sys
import itertools
import math

class Location(object):
    def __init__(self, name, x, y, price, perish):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.price = int(price)
        self.perish = perish

    def __repr__(self):
        return "%s:%d" % (self.name, self.price)

class Item(object):
    def __init__(self, name):
        self.name = name
        self.perish = (name[-1] == '!')
        self.locations = []

    def add_location(self, x, y, price):
        l = Location(self.name, x, y, price, self.perish)
        self.locations.append(l)
    
def distance(xa, ya, xb, yb):
    return math.sqrt((xa - xb)**2 + (ya - yb)**2)

def calculate_route(route, gasprice):
    x, y = 0, 0
    price = 0
    for l in route:
        price += gasprice * distance(x, y, l.x, l.y)
        x, y = l.x, l.y
        price += l.price
        if l.perish:
            price += gasprice * distance(l.x, l.y, 0, 0)
            x, y = 0, 0
    price += gasprice * distance(x, y, 0, 0)
    return price

def item_list_price(choice, gasprice):
    min_price = 99999999
    winner_route = ()
    for order in itertools.permutations(choice):
        price = calculate_route(order, gasprice)
        if price < min_price:
            min_price = price
            winner_route = order
    return min_price, order

def debug_print(req_items, items):
    print req_items
    for item in items.keys():
        if items[item].perish:
            print "Perishable: " + item 
        else:
            print item
        for i in items[item].locations:
            print "\t [%d, %d] : %d" % (i.x, i.y, i.price)


def Solve():
    [nitems, nstores, gasprice] = map(int, sys.stdin.readline().split())
    req_items = sys.stdin.readline().split()
    # We create a hash table with item name being the key. Each element will
    # contain a list of Items, which stores the location and price of an item in
    # a particular store
    items = {}
    for name in req_items:
        items[name.strip('!')] = Item(name)

    index = 0
    while index < nstores:
        line = sys.stdin.readline().split()
        (x, y)  = (line[0], line[1])
        line = line[2:]
        for product in line:
            [item, price] = product.split(':')
            items[item].add_location(x, y, price)
        index += 1

    all = []
    for item in items.keys():
        all.append(items[item].locations)

    p = 999999999
    winner = ()
    for a in itertools.product(*all):     
        (np, order) = item_list_price(a, gasprice)
        if np < p:
            p = np
            winner = order
            
    return round(p, 7)

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %0.7f" % (case, Solve())
