#!/usr/bin/python
# Works only with small solution...

import sys
import math

class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def distance_with(self, b):
        return math.sqrt((b.x - self.x)**2 + (b.y - self.y)**2)

class Triangle(object):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
        self.ab = a.distance_with(b)
        self.ac = a.distance_with(c)
        self.bc = b.distance_with(c)
        self.perimeter = self.ab + self.ac + self.bc

    def get_area(self):
        s = self.perimeter / 2
        return math.sqrt(s * (s - self.ab) * (s - self.ac) * (s - self.bc))

    def calculate_angles(self):
        self.a_angle = math.acos((self.ab**2 + self.ac**2 - self.bc**2) / (2 * self.ab * self.ac))
        self.b_angle = math.acos((self.ab**2 + self.bc**2 - self.ac**2) / (2 * self.ab * self.bc))
        self.c_angle = math.acos((self.ac**2 + self.bc**2 - self.ab**2) / (2 * self.ac * self.bc))

def eq(a, b):
    d = abs(a - b)
    if d < 0.00001:
        return True
    return False

def Solve():
    coords = map(int, sys.stdin.readline().split())
    a = Point(coords[0], coords[1])
    b = Point(coords[2], coords[3])
    c = Point(coords[4], coords[5])
    t = Triangle(a, b, c)

    if (t.get_area() == 0):
        return "not a triangle"

    if (t.ab == t.ac) or (t.ab == t.bc) or (t.ac == t.bc):
        sides = "isosceles"
    else:
        sides = "scalene"

    t.calculate_angles()

    la = math.pi / 2

    if eq(t.a_angle, la) or eq(t.b_angle, la) or eq(t.c_angle, la):
    #if t.a_angle == la or t.b_angle == la or t.c_angle == la:
        angles = "right"
    elif t.a_angle > la or t.b_angle > la or t.c_angle > la:
        angles = "obtuse"
    else:
        angles = "acute"

    return "%s %s triangle" % (sides, angles)

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s" % (case, Solve())
