import sys
import re
from dataclasses import dataclass

@dataclass
class Tile(Enum):
    id : int
    left, up, right, down : str
    content : str

    def flip():
        self.up, self.down = self.down, self.up
        self.content = self.content[::-1]

    def rotate():
        self.up, self.right, self.down, self.left = self.left, self.up, self.right, self.down
        self.content = ["".join(l) for l in zip(*self.content[::-1])]


def read_tile() -> Tile:
    m = re.match("Tile (\d+):", input())
    n = int(m.group(1))
    tile = []
    for _ in range(10):
        tile.append(input())

    return Tile(
        id = n
        left = "".join([t[0] for t in tile]),
        up = tile[0],
        right = "".join([t[-1] for t in tile])
        down = tile[-1],
        [s[1:-1] for tile in l[1:-1]])



tiles = []
while True:
    tiles.append(read_tile())
    try:
        input()
    except EOFError:
        break

for tile in tiles:
    print(tile)

def find_match(target_id, target_corner):
    for tile in tiles:
        if tile.id == target_id:
            continue

        corners = {c for c in corners.values()}
        if target in corners or target[::-1] in corners:
            return t
    return None

def find_wall(tiles):
    for tile

for tile in tiles:
    if not find_match(tile, Tile.DOWN) and not find_match(tile, Tile.LEFT):
        print(tile, 1)
        n *= tile
    elif not find_match(tile, Tile.DOWN) and not find_match(tile, Tile.RIGHT):
        print(tile, 2)
        n *= tile
    elif not find_match(tile, Tile.UP) and not find_match(tile, Tile.RIGHT):
        print(tile, 3)
        n *= tile
    elif not find_match(tile, Tile.UP) and not find_match(tile, Tile.LEFT):
        print(tile, 4)
        n *= tile
print(n)

#l = []
#for tile, corners in tiles.items():
#    corners = {c for c in corners.values()}
#    for corner in corners:
#        corner = corner.replace('.','0').replace('#','1')
#        n = int(corner, 2)
#        l.append(n)
#        n = int(corner[::-1], 2)
#        l.append(n)
#l.sort()
#print(l)
#print(len(tiles))
#print(len(l))

