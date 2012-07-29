#!/usr/bin/env python3

import sys

for a in range(1, 1000):
  for b in range(a, 1000):
    for c in range(b, 1000):
      if ((a + b + c) == 1000) and ((a*a + b*b) == c*c):
        print(a*b*c)
        sys.exit(0)
