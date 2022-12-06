#!/usr/bin/env python
import sys

numbers = {
    2: [ (1, set('cf')) ],
    3: [ (7, set('acf')) ],
    4: [ (4, set('bcdf')) ],

    5: [ 
         (2, set('acdeg')), 
         (3, set('acdfg')), 
         (5, set('abdfg')),
       ],
    
    6: [ 
         (0, set('abcefg')), 
         (6, set('abdefg')), 
         (9, set('abcdfg')),
       ],
    7: [ (8, set('abcdefg')) ]
}

def options(size):
    s = set()
    for number in numbers[size]:
        s |= number[1]
    return s

def must(size):
    s = set('abcdefg')
    for number in numbers[size]:
        s &= number[1]
    return s

def translate(word, matching):
    s = ''
    for c in word:
        if len(matching[c]) == 1:
            s += list(matching[c])[0]
        else:
            s += '?'
    return set(s)

def search(training, output):
    matching = {}
    for c in 'abcdefg':
        matching[c] = set('abcdefg')

    for number in training:
        size = len(number)
        for c in 'abcdefg':
            if c in number:
                matching[c] &= options(size)
            else:
                matching[c] -= must(size)

    # Further resolve matching. If a letter is already resolved, we can remove it from all the others
    for c, v in matching.items():
        if len(v) == 1:
            a = list(matching[c])[0]
            for c2, v2 in matching.items():
                if c2 != c:
                    v2 -= set(a)
    
    number = 0
    for word in output:
        sword = translate(word, matching)
        for l in numbers.values():
            for n, s in l:
                if sword == s:
                    number = 10 * number + n
    return number

total = 0
for line in sys.stdin:
    training, output = line.split(' | ')
    training = training.split()
    output = output.split()
    print(training, output)
    total += search(training, output)

print(total)
