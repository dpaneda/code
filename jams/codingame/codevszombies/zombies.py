import sys
import math
import operator
from collections import namedtuple

# Posible improvements in: triangle, flanked


def distance(pos, pos2):
    sq1 = (pos.x - pos2.x) * (pos.x - pos2.x)
    sq2 = (pos.y - pos2.y) * (pos.y - pos2.y)
    return math.sqrt(sq1 + sq2)


def dead(pos, human, zombies):
    if not zombies:
        return False

    # If some zombie is able to reach this person before me, I consider
    # this human dead. This is not completely correct because the zombies
    # always move to the nearest person
    zombie = nearest_person(human, zombies)

    zombie_distance = distance(human, zombie)
    my_distance = distance(human, pos) - 2000

    zombie_time = math.ceil(zombie_distance / 400)
    my_time = math.ceil(my_distance / 1000)

    if zombie_time < my_time:
        print >>sys.stderr, "Human {} dead by {} ({} {} {} {})".format(human, zombie, my_distance, zombie_distance, my_time, zombie_time)
    return zombie_time < my_time


def calculate_delta(pos, target, mov):
    if (distance(pos, target) < mov):
        p = Point(target.x - pos.x, target.y - pos.y)
    if (target.x - pos.x == 0):
        p = Point(0, mov)
    else:
        m = abs(target.y - pos.y) / float(abs(target.x - pos.x))
#    print >>sys.stderr, "m", pos, target, m
        xdelta = math.sqrt(mov ** 2 / (1 + m ** 2))
        ydelta = m * xdelta
        p = Point(int(xdelta), int(ydelta))
    if pos.x > target.x:
        p = Point(-p.x, p.y)
    if pos.y > target.y:
        p = Point(p.x, -p.y)
    return p


def fib(n):
    sqrt = math.sqrt
    return ((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5))


def simulate(pos, target, humans, zombies):
    turns = math.ceil((distance(pos, target) - 2000) / 1000)
    turns = int(turns)
    points = 0

    humans = list(humans)
    zombies = list(zombies)

    print >>sys.stderr, "Simulating going to {} in {}".format(target, turns)

    for i in xrange(turns):
        delta = calculate_delta(pos, target, 1000)
        pos = Point(pos.x + delta.x, pos.y + delta.y)
        if humans:
            for i in xrange(len(zombies)):
                victim = nearest_person(zombies[i], humans)
                d = calculate_delta(zombies[i], victim, 400)
                zombies[i] = Point(zombies[i].x + d.x, zombies[i].y + d.y)

        nzombies = len(zombies)
        zombies = filter(lambda z: distance(pos, z) > 2000, zombies)
        zk = nzombies - len(zombies)
        for i in xrange(zk):
            if i > 0:
                points += ((len(humans) ** 2) * 10) * fib(i + 2)
            else:
                points += ((len(humans) ** 2) * 10)

        def will_survive(human):
            for zombie in zombies:
                if human == zombie:
                    return False
            return True

        nhumans = len(humans)
        humans = filter(will_survive, humans)
        hk = nhumans - len(humans)
        print >>sys.stderr, "Pos {} ZK {} HK {} Points {}".format(pos, zk, hk, points)
#        print >>sys.stderr, humans, zombies
    if turns == 0:
        return points
    else:
        return points / float(turns)


def calculate_lifespan(humans, zombies):
    life = {}
    for human in humans:
        zombie = nearest_person(human, zombies)
        dist = distance(human, zombie)
        turns = math.ceil(dist / 400.0)
        life[human] = turns
    return life


def nearest_person(whom, humans):
    return sort_persons(whom, humans)[0]


def sort_persons(pos, humans):
    def distance_to_me(h):
        return distance(pos, h)

    return sorted(humans, key=distance_to_me, reverse=False)

Point = namedtuple('Point', ['x', 'y'])

while 1:
    #print 4000, 5500
    #continue
    x, y = [int(i) for i in raw_input().split()]
    human_count = int(raw_input())

    humans = []
    zombies = []
    zombies_deltas = []

    pos = Point(x, y)

    for i in xrange(human_count):
        human_id, human_x, human_y = [int(j) for j in raw_input().split()]
        humans.append(Point(human_x, human_y))

    zombie_count = int(raw_input())
    for i in xrange(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in raw_input().split()]
        zombies.append(Point(zombie_x, zombie_y))
        zombies_deltas.append(Point(zombie_xnext - zombie_x, zombie_ynext - zombie_y))

    humans = sort_persons(pos, humans)
    lifes = calculate_lifespan(humans, zombies)
    sorted_lifes = sorted(lifes.items(), key=operator.itemgetter(1))
    target = None

    print >>sys.stderr, "Humans", humans, lifes

#    best_points = 0
#    best = humans[0]

#    for human in humans:
#        if dead(pos, human, zombies):
#            print >>sys.stderr, "Human dead: {}", human
#            continue
#        target = nearest_person(human, zombies)
#        p = simulate(pos, human, humans, zombies)
#        print >>sys.stderr, "Points", human, p
#        if p > best_points:
#            best = human
#            best_points = p

    for v in sorted_lifes:
        human = v[0]
        if dead(pos, human, zombies):
            print >>sys.stderr, "Human dead: {}", human
            continue
        target = human
        break

    # The target will be the nearest zombie to the person to protect
    #print >>sys.stderr, zombies
    target = nearest_person(target, zombies)
    #target = best

    if target and distance(pos, target) > 1900:
        print target.x, target.y
    else:
        print pos.x, pos.y
