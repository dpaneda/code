#!/usr/bin/python

import sys
import time

# Number of leds of each number
digit_led = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

def count_leds(time):
    leds = 0
    for num in (time.tm_hour, time.tm_min, time.tm_sec):
        leds += digit_led[num % 10]
        leds += digit_led[num / 10]
    return leds

for line in sys.stdin:
    seconds = int(line)
    zero = -3600
    leds = 0
    for i in xrange(seconds +1):
        leds += count_leds(time.localtime(zero + i))
    print leds
