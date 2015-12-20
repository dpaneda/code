import sys
import math

# Save humans, destroy zombies!


# game loop
while 1:
    x, y = [int(i) for i in raw_input().split()]
    human_count = int(raw_input())
    for i in xrange(human_count):
        human_id, human_x, human_y = [int(j) for j in raw_input().split()]
    zombie_count = int(raw_input())
    for i in xrange(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in raw_input().split()]

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # Your destination coordinates
    print "0 0"
