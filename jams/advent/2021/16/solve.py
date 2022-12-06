#! /usr/bin/env python
from __future__ import annotations
from typing import List
from dataclasses import dataclass
import math
import operator

@dataclass
class Packet:
    version : int
    type_id : int
    size    : int
    value   : int
    content : List[Packet]

    def version_sum(self):
        return self.version + sum(map(lambda o: o.version_sum(), self.content))
    
    def resolve_childs(self):
        return map(lambda o: o.resolve(), self.content)

    def resolve(self):
        type_id_to_op = [sum, math.prod, min, max, None, operator.gt, operator.lt, operator.eq]
        match self.type_id:
            case 4: return self.value
            case 5 | 6 | 7:
                return type_id_to_op[self.type_id](*self.resolve_childs())
            case _:
                return type_id_to_op[self.type_id](self.resolve_childs())

def read_int(raw):
    nbin = ''
    i = 0 
    while raw[i] == '1':
        nbin += raw[i+1:i+5]
        i += 5
    nbin += raw[i+1:i+5]
    return int(nbin, 2), i+5

def read_packet(raw):
    version = int(raw[:3], 2)
    type_id = int(raw[3:6], 2)
    value = 0
    content = []
    size = 6
    if type_id == 4:
        n, nsize = read_int(raw[6:])
        value = n
        size += nsize
    else:
        lenght_id = raw[6]
        if lenght_id == '0':
            remain_size = int(raw[7:7+15], 2)
            raw = raw[22:]
            size += 16
            while remain_size > 0:
                packet = read_packet(raw)
                size += packet.size
                raw = raw[packet.size:]
                content.append(packet)
                remain_size -= packet.size
        else:
            remain_to_read = int(raw[7:7+11], 2)
            raw = raw[18:]
            size += 12
            for _ in range(remain_to_read):
                packet = read_packet(raw)
                size += packet.size
                raw = raw[packet.size:]
                content.append(packet)
    return Packet(version, type_id, size, value, content)

raw = bin(int('1'+input(), 16))[3:]

packet = read_packet(raw)
print(packet.version_sum())
print(packet.resolve())
