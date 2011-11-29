#!/usr/bin/python

import sys
import time

dig = \
[\
" _ "\
"| |"\
"|_|",

"   "\
"  |"\
"  |",

" _ "\
" _|"\
"|_ ",

" _ "\
" _|"\
" _|",

"   "\
"|_|"\
"  |",

" _ "\
"|_ "\
" _|",

" _ "\
"|_ "\
"|_|",

" _ "\
"  |"\
"  |",

" _ "\
"|_|"\
"|_|",

" _ "\
"|_|"\
" _|",

"   "\
"   "\
"   "\
]

def count_diff(a, b):
    t = 0
    for i in xrange(9):
        # If the led has changed and previously was turned off
        if dig[a][i] != dig[b][i] and dig[a][i] == ' ':
            t += 1
    return t

def count_leds(clock, time):
    leds = 0
    numbers = [time.tm_hour / 10, 
               time.tm_hour % 10,
               time.tm_min / 10,
               time.tm_min % 10,
               time.tm_sec / 10,
               time.tm_sec % 10]

    for i in xrange(6):
        leds += count_diff(clock[i], numbers[i])

    return leds, numbers

for line in sys.stdin:
    seconds = int(line)
    zero = -3600
    leds = 0
    clock = [10, 10, 10, 10, 10, 10]
    for i in xrange(seconds +1):
        nleds, clock = count_leds(clock, time.localtime(zero + i))
        leds += nleds
    print leds
