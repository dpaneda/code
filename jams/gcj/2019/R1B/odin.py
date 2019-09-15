import sys
import os

W = 6

def solve():
    d = [0]
    for i in xrange(1, W+1):
        print(i)
        sys.stdout.flush()
        d.append(input())
   
    delta2 = d[2] - d[1]
    delta3 = d[3] - d[2]
    delta4 = d[4] - d[3]
    delta5 = d[5] - d[4]
    delta6 = d[6] - d[5]

    for d1 in xrange(101):
        for d2 in xrange(101):
            if d1 + d2 != delta2:
                continue
            for d3 in xrange(101):
                if d1 + d3 != delta3:
                    continue
                for d4 in xrange(101):
#                    if delta4 != d1 + d2 + d4:
#                        continue
                    for d5 in xrange(101):
#                        if delta5 != d1 + d5:
#                            continue
                        for d6 in xrange(101):
                            if d1 + d1 + d2 + d3 + d4 + d5 + d6 == d[1]:
                                return " ".join(map(str,[d1, d2, d3, d4, d5, d6]))

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
cases, w = map(int, raw_input().split())
for case in xrange(cases):
    print(solve())
