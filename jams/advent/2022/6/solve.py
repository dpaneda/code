#! /usr/bin/env python

line = input()
markers = [4, 14]
for m in markers:
    for i in range(0, len(line)):
        if len(set(line[i-m:i])) == m:
            print(f"Marker {m} is at position {i}")
            break
