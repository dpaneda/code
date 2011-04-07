#!/usr/bin/env python

import sys
from scapy import *
conf.verb=0

if len(sys.argv) != 3:
    print "Usage: ./firewalk.py <target> <dport>"
    sys.exit(1)

dest=sys.argv[1]
port=sys.argv[2]

ttl = 0

def mkicmppacket():
    global ttl
    ttl = ttl + 1
    p = IP(dst=dest, ttl=ttl)/ICMP()
    return p

def mktcppacket():
    global ttl, dest, port
    ttl = ttl + 1
    p = IP(dst=dest, ttl=ttl)/TCP(dport=int(port), flags="S")
    return p

res = sr1(mkicmppacket())
while res.type == 11:
    res = sr1(mkicmppacket())
    print "+"

nat_ttl = ttl
# Since we now know our minimum TTL, we don't need to reset TTL to zero
# We do need to decrease TTL or otherwise mkpacket will increase it again
# which would result in every port being detected as forwarded
ttl = ttl - 1

res = sr(mktcppacket(),timeout=10)
while res.proto == 1 and res.type == 11:
    res = sr(mktcppacket(),timeout=10)

if res.proto != 6:
    print "Error"
    sys.exit(1)

if nat_ttl == ttl: print "Not NATed (" + str(nat_ttl) + ", " + str(ttl) + ")"
else: print "This port is NATed. firewall TTL is " + str(nat_ttl) + ", TCP port TTL is " + str(ttl)

sys.exit(0)

