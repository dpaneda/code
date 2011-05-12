#!/usr/bin/python
import sys

num = int(sys.stdin.readline())
cached = {}

sys.setrecursionlimit(100000)

def is_sure_win(i, j):
   if i < j:
      a = i
      b = j
   else:
      a = j
      b = i

   h = str(a) + '/' + str(b)
   if not cached.has_key(h):
      cached[h] = is_sure_win_not_cached(a, b)
   return cached[h]

def is_sure_win_not_cached(a, b):
    # Just to make thing cleaner, we put in a the lower one
    if a == b:
        return False

    if b % a == 0:
        return True

    if a + 1 == b:
        return False

    if ((b + 1) % a) == 0:
        return True

    if ((b - 1) % a) == 0:
        return True

    if b < (a * 2):
        return not is_sure_win(a, b - a)

    k = b / a
    i = 1

    while i <= k:
        if not is_sure_win(a, b - i * a):
            return True
        i += 1

    return False

for case in range(1, num+1):
    [a1, a2, b1, b2] = map(int, sys.stdin.readline().split())
    #print a1, a2, b1, b2

    count = 0
    i = a1
    while i <= a2:
        j = b1
        while j <= b2:
            if is_sure_win(i, j):
                #print i, j
                count += 1
            j += 1
        i += 1   

    print "Case #%d: %d" % (case, count)
