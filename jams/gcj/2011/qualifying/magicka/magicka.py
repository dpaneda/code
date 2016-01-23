#!/usr/bin/python

import sys

num = int(sys.stdin.readline())

def do_combine(book, a, b):
    if (book.has_key(a + b)):
        return book[a + b]
    if (book.has_key(b + a)):
        return book[b + a]
    return None

def is_in(x, seq):
    for item in seq:
        if item == x:
            return True
    return False

for case in range(1, num + 1):
    combine = {}
    opposed = {}
    wizard_book = sys.stdin.readline().split()
    combinations = int(wizard_book[0])

    i = 1
    while i < combinations + 1:
        recipe = wizard_book[i][:-1]
        result = wizard_book[i][2:]
        combine[recipe] = result
        i += 1

    opposeds = int(wizard_book[i])

    i += 1
    while i < combinations + opposeds + 2:
        yin = wizard_book[i][0]
        yan = wizard_book[i][1]
        opposed[yin] = yan
        i += 1

    invocation = list(wizard_book[combinations + opposeds + 3])

    final_invocation = []
    for element in invocation:
        final_invocation.append(element)
        if len(final_invocation) >= 2:
            res = do_combine(combine, final_invocation[-2], final_invocation[-1])
            if res:
                # Remove old elements and insert the result of combination 
                final_invocation = final_invocation[:-2]
                final_invocation.append(res)

        for yin, yan in opposed.items():
            if is_in(yin, final_invocation) and is_in(yan, final_invocation):
                final_invocation = []

    invocation_str = str(final_invocation).replace("'","")

    print "Case #%d: %s" % (case, invocation_str)
