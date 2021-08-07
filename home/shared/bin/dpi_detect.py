#! /usr/bin/env python
import subprocess
import re
import os

os.environ['DISPLAY'] = ':0'

def mm_to_inch(n : int):
    return n / (10 * 2.54)

process = subprocess.run(["xrandr"], capture_output=True)
for line in process.stdout.splitlines():
    m = re.search("(\w+) connected (primary)? (\d+)x(\d+).* (\d+)mm x (\d+)mm", line.decode())
    if m:
        groups = list(m.groups())
        name = groups.pop(0)
        primary = groups.pop(0)
        xres, yres, xsize, ysize = map(int, groups)
        xdpi = xres // mm_to_inch(xsize)
        ydpi = yres // mm_to_inch(ysize)
        print(f"{name} screen ({xres}x{yres}) - DPI: {xdpi} {ydpi}")
