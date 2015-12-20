#!/usr/bin/python2

import sys

cases = int(raw_input())

def are_cheaters(students, Q, S, answers):
    max_cheaters = (students + 1) / 2
    searched = []

    def search_string(match, pos):
        if match in searched:
            return False
        cheaters = sum([1 for a in answers if 0 == a[pos:].find(match)])
        searched.append(match)
        return cheaters >= max_cheaters

    for ref_class in xrange(len(answers)):
        for i in xrange(0, Q - S + 2):
            match = answers[ref_class][i:S+i]
            pos = answers[ref_class].find(match)
            if search_string(match, pos):
                return True
    return False

for cases in xrange(cases):
    C, Q, A, S = map(int, raw_input().strip().split())
    cheaters = []
    for c in xrange(C):
        class_info = raw_input().split()
        students = int(class_info.pop(0))
        if are_cheaters(students, Q, S, class_info):
            cheaters.append(c)
    cheaters = map(str, cheaters)
    print " ".join(cheaters)
