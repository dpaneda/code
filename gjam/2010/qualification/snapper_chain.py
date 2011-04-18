#!/usr/bin/python
from GoogleJam import GoogleJam

def Resolve(case):
    n, k = int(case[0]), int(case[1])
    
    chain_mask = (1 << n) - 1
    if (k & chain_mask) == chain_mask:
        return "ON"
    return "OFF"

GoogleJam(Resolve)
