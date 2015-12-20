#!/usr/bin/python2

import sys


def possible(word, keyboard):
    for c in word:
        if c not in keyboard:
            return False
    return True


def word_odds(word, keyboard):
    odds = 1.0
    for c in word:
        odds *= float(keyboard.count(c)) / len(keyboard)
    return odds


def max_occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count += 1
        else:
            return count



def min_repetition(word):
    for i in xrange(1, len(word)):
        if max_occurrences(word + word[-i:], word) == 2:
            return i
    return len(word)

def solve():
    K, L, S = map(int, sys.stdin.readline().split())
    keyboard = sys.stdin.readline().strip()
    word = sys.stdin.readline().strip()

#    print K, L, S, word, keyboard
    if not possible(word, keyboard):
        return 0.0

    if S < L:
        return 0.0

    rep = min_repetition(word)
#    print rep

    if rep == len(word):
        s = (word * (S / L)) + word[:(S % L)]
    else:
        s = word
        s += word[-rep:] * ((S - L) / rep)
        s += word[: S - len(s)]

#    over = detect_overlap(word)
#    if over == 0:
#        s = (word * (S / L)) + word[:(S % L)]
#    else:
#        s = word
#        s += word[over:] * ((S - L) / (L - over))
#        s += word[: S - len(s)]

#    print s

#    max_oc = 0
#    for i in xrange(L):
#        s = (word * (S / L)) + word[i:(S % L) + i]
#        oc = max_occurrences(s, word)
#        if oc > max_oc:
#            max_oc = oc

    bananas = max_occurrences(s, word)

#    print "Bring %d, expected for word, %f" %(bananas, word_odds(word, keyboard))
    expected = (S - L + 1) * word_odds(word, keyboard)
    return bananas - expected


num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print "Case #{0}: {1}".format(case, solve())
