#!/usr/bin/python3
import math

def solve():
    perc, x, y = list(map(int, input().split()))
    x -= 50
    y -= 50
    point_degree = math.degrees(math.atan2(y, x))
    r = math.sqrt(x * x + y * y)
    degree = (perc * 360) / 100

    if point_degree <= degree and r <= 50:
        return 'black'
    return 'white'

num = int(input())

for case in range(1, num + 1):
    print("Case #%d: %s " % (case, solve()))
