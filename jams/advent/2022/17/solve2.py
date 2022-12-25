#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from pygame import Rect
import pygame
import numpy as np


GRID_WIDTH, GRID_HEIGHT = 21, 220
TILE_SIZE = 3

WIDE = GRID_WIDTH // TILE_SIZE
HEIGHT = GRID_HEIGHT // TILE_SIZE

class BottomReached(Exception):
    pass

h = [ ]

class Block(pygame.sprite.Sprite):
    
    @staticmethod
    def collide(block, group):
        """
        Check if the specified block collides with some other block
        in the group.
        """
        for other_block in group:
            # Ignore the current block which will always collide with itself.
            if block == other_block:
                continue
            if pygame.sprite.collide_mask(block, other_block) is not None:
                return True
        return False
    
    def __init__(self, moves, height = 10):
        super().__init__()
        # Get a random color.
        self.color = (123, 123, 200)
        self.current = True
        self.struct = np.array(self.struct)
        self._draw(2, HEIGHT - height - 3 - len(self.struct))
    
    def _draw(self, x, y):
        width = len(self.struct[0]) * TILE_SIZE
        height = len(self.struct) * TILE_SIZE
        self.image = pygame.surface.Surface([width, height])
        self.image.set_colorkey((0, 0, 0))
        # Position and size
        self.rect = Rect(0, 0, width, height)
        self.x = x
        self.y = y
        for y, row in enumerate(self.struct):
            for x, col in enumerate(row):
                if col:
                    pygame.draw.rect(
                        self.image,
                        self.color,
                        Rect(x*TILE_SIZE + 1, y*TILE_SIZE + 1,
                             TILE_SIZE - 2, TILE_SIZE - 2)
                    )
        self._create_mask()
    
    def redraw(self):
        self._draw(self.x, self.y)
    
    def _create_mask(self):
        """
        Create the mask attribute from the main surface.
        The mask is required to check collisions. This should be called
        after the surface is created or update.
        """
        self.mask = pygame.mask.from_surface(self.image)
    
    def initial_draw(self):
        raise NotImplementedError
    
    @property
    def group(self):
        return self.groups()[0]
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value
        self.rect.left = value*TILE_SIZE
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value
        self.rect.top = value*TILE_SIZE
    
    def move_left(self, group):
        self.x -= 1
        # Check if we reached the left margin.
        if self.x < 0 or Block.collide(self, group):
            self.x += 1
    
    def move_right(self, group):
        self.x += 1
        # Check if we reached the right margin or collided with another
        # block.
        if self.rect.right > GRID_WIDTH or Block.collide(self, group):
            # Rollback.
            self.x -= 1
    
    def move_down(self, group, jet_move):
        if jet_move == '<':
            self.move_left(group)
        if jet_move == '>':
            self.move_right(group)
        self.y += 1
        if self.rect.bottom > GRID_HEIGHT or Block.collide(self, group):
            # Rollback to the previous position.
            self.y -= 1
            self.color = (123, 123, 123)
            self.redraw()
            self.current = False
            raise BottomReached
    
    def update(self):
        if self.current:
            self.move_down()


class HLineBlock(Block):
    struct = (
        (1, 1, 1, 1),
    )

class PlusBlock(Block):
    struct = (
        (0, 1, 0),
        (1, 1, 1),
        (0, 1, 0)
    )

class LBlock(Block):
    struct = (
        (0, 0, 1),
        (0, 0, 1),
        (1, 1, 1)
    )

class VLineBlock(Block):
    struct = (
        (1,),
        (1,),
        (1,),
        (1,)
    )

class SquareBlock(Block):
    struct = (
        (1, 1),
        (1, 1),
    )


class BlocksGroup(pygame.sprite.OrderedUpdates):
    
    def __init__(self, moves, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self._ignore_next_stop = False
        # Not really moving, just to initialize the attribute.
        self.stop_moving_current_block()
        self.blocks = (HLineBlock, PlusBlock, LBlock, VLineBlock, SquareBlock)
        self.block_count = 0
        self.next_block = 0
        self.moves = np.array(list(moves))
        self.height = 0
        self._create_new_block()
    
    def _create_new_block(self):
        new_block = self.blocks[self.next_block](self.moves, self.height)
        self.next_block = (self.next_block + 1) % len(self.blocks)
        self.add(new_block)
    
    @property
    def current_block(self):
        return self.sprites()[-1]
    
    def update_current_block(self):
        try:
            self.current_block.move_down(self, self.moves[0])
        except BottomReached:
            self.block_count += 1
            self.last_height = self.height
            self.height = max(HEIGHT - self.current_block.y, self.height)
            diff = self.height - self.last_height
            h.append(diff)
            self.stop_moving_current_block()
            self._create_new_block()
            if self.block_count % 500:
                print(self.block_count, self.height)
        self.moves = np.roll(self.moves, -1)
    
    def stop_moving_current_block(self):
        if self._ignore_next_stop:
            self._ignore_next_stop = False
        else:
            self._current_block_movement_heading = None

def draw_centered_surface(screen, surface, y):
    screen.blit(surface, (400 - surface.get_width()/2, y))

def search_loop(h):
    for loop_size in range(1690, 1691):
      for j in range(1780, 1781):
        bad = False
        for i in range(0, loop_size):
            if h[i+j] != h[i + j + loop_size]:
                bad = True
        if not bad:
            print(f"Looks good: {loop_size} at j {j}")
            loop_value = sum(h[i+j:i + j + loop_size])
            print(f"Loop value: {loop_value}, extra: {sum(h[:j])}")
            print((loop_value * ((1000000000000 - j) // loop_size)) + sum(h[:j]))
            print(h[:j])
            print(h[j:j+loop_size])
            return True
    return False

def main():
    moves = input()
    blocks = BlocksGroup(moves)
    
    while blocks.block_count < 4000:
        blocks.update_current_block()

    print(blocks.block_count, blocks.height)
    search_loop(h)
    pygame.quit()

if __name__ == "__main__":
    main()
