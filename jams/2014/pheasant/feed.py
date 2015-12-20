#!/usr/bin/python2

import sys
import string

from Crypto.Cipher import AES
from itertools import product
import bisect


def get_user_data(id):
    mod = str(id % 100).zfill(2)
    last_file = "output/last_times/%s/%s.timestamp" % (mod, id)
    feed_file = "output/encrypted/%s/%s.feed" % (mod, id)
    last_time = int(open(last_file).read())
    feed = open(feed_file).read()
    return [last_time, feed]


def decrypt(encrypted_data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(encrypted_data)


def crack(user_id, encrypted_data, key):
    for s in product(string.letters, repeat=3):
        key_try = key + ''.join(s)
        out = decrypt(encrypted_data, key_try)
        if out.startswith(str(user_id)):
            out = filter(lambda x: x in string.printable, out)
            a = [map(int, l.split()) for l in out.splitlines()]
            a = filter(len, a)
            return a


input_data = sys.stdin.readline().strip().split(';')
needed_events = int(input_data[0])

# List of the lasttimes ordered
events = []

# Data of the events indexed by lasttime
events_data = {}
ready_events = []

for i in input_data[1:]:
    user_data = i.split(',')
    user_id = int(user_data[0])
    last, feed_data = get_user_data(user_id)
    bisect.insort_left(events, last)
    events_data[last] = [user_id, feed_data, user_data[1]]


while needed_events:
    last = events.pop()
    data = crack(*events_data[last])
    for d in data:
        bisect.insort_left(ready_events, d[1])
        events_data[d[1]] = d[2]

    while ready_events and ready_events[-1] > events[-1]:
        print events_data[ready_events.pop()],
        needed_events -= 1
