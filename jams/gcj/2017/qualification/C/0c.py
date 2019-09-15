import sys, math

cases = int(raw_input())
for case in xrange(1, cases+1):
    [n, k] = [int(x) for x in raw_input().split(' ')]
    group = k.bit_length() - 1
    groupStart = 2 ** group
    groupSize = groupStart
    groupOffset = k - groupStart
    groupDivisor = groupStart * 2
    
    maxMin = (n - groupOffset - groupSize) // groupDivisor
    maxMax = (n - groupOffset) // groupDivisor
    
    print "Case #%d: %d %d" % (case, maxMax, maxMin)
