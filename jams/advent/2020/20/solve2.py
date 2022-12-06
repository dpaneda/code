import sys
import re
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Tile():
    id : int
    left : str
    up : str
    right :str
    down : str
    content : List[str]

    def flip(self):
        self.up, self.down = self.down, self.up
        self.content = self.content[::-1]

    def rotate(self):
        self.up, self.right, self.down, self.left = self.left, self.up, self.right, self.down
        self.content = ["".join(l) for l in zip(*self.content[::-1])]

    def __repr__(self):
        s = f"Tile {self.id}:\n"
        for s2 in self.content:
            s += s2 + "\n"
        return s

@dataclass
class Position():
    x : int
    y : int

@dataclass
class Grid():
    n : int
    grid : Dict[Position, Tile]

    def __init__(self, n : int):
        self.n = n
        self.grid = {}

    def get_corners(self, p : Position) -> Dict[str, str]:
        neighbohrs = {
            'left':  (p.x - 1, p.y),
            'up':    (p.x, p.y - 1),
            'right': (p.x + 1, p.y),
            'down':  (p.x, p.y + 1)
        }
        corners = {}
        for corner, (x, y) in neighbohrs.items():
            if x < 0 or y < 0 or x > self.n or y > self.n:
                corners[corner] = "WALL"
            else:
                tile = self.grid.get(Position(x, y), None)
                corners[corner] = getattr(tile, corner) if tile else None
        return corners


def read_tile() -> Tile:
    m = re.match("Tile (\d+):", input())
    if m:
        n = int(m.group(1))
    tile = []
    for _ in range(10):
        tile.append(input())

    return Tile(
        id = n,
        left = "".join([t[0] for t in tile]),
        up = tile[0],
        right = "".join([t[-1] for t in tile]),
        down = tile[-1],
        content = [s[1:-1] for s in tile[1:-1]])

tiles = {}
tiles_done : Dict[int, Tile] = {}
while True:
    tile = read_tile()
    tiles[tile.id] = tile
    try:
        input()
    except EOFError:
        break

#for tid, tile in tiles.items():
#    print(tile)

def find_corner(target_id, corner):
    for tid, tile in tiles.items():
        if tid == target_id:
            continue
        
        for _ in range(2):
            for _ in range(4):
                if tile.left == target_corner:
                    return tile
                tile.rotate()
            tile.flip()
    return None


def find_match(target_id, target_corner):
    for tid, tile in tiles.items():
        if tid == target_id:
            continue
        
        for _ in range(2):
            for _ in range(4):
                if tile.left == target_corner:
                    return tile
                tile.rotate()
            tile.flip()
    return None

def find_wall(tiles):
    for tid, tile in tiles.items():
        if not find_match(tid, tile.right):
            print(tid)

find_wall(tiles)
