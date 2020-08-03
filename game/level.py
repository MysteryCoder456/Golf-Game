import pygame
from glm import vec2

from .tile import Tile

class Level:
    def __init__(self, win_size: vec2, tile_size: int = 34, tile_map=None):
        self.tile_size = int(tile_size)

        while not (win_size.x % self.tile_size == 0 and win_size.y % self.tile_size == 0):
            self.tile_size -= 1

        self.cols = int(win_size.x / self.tile_size)
        self.rows = int(win_size.y / self.tile_size)

        if tile_map == None:
            # resolution = 30x21
            self.tile_map = [
                "000000000000000000000000000000",
                "000000000000000000000000000000",
                "000000000000000000000000000000",
                "000000000000000000000000000000",
                "000000000000000000000000000000",
                "000000000000000000000000000000",
                "000000000000001100000000000000",
                "000000000000001100000000000000",
                "000000000000001100000000000000",
                "000000000000001100000000000000",
                "000000000011111111110000000000",
                "000000000011111111110000000000",
                "000000000000001100000000000000",
                "000000000000001100000000000000",
                "000000000000001100000000000000",
                "000000000000001100000000000000",
                "000000000000000000000000000000",
                "000000000000000000000000000000",
                "000000000000000000000000000000",
                "000000000000000000000000000000",
                "000000000000000000000000000000"
            ]
        else:
            self.tile_map = tile_map

    def build_level(self):
        tiles = []
        tile_map = self.tile_map
        try:
            for y in range(self.rows):
                for x in range(self.cols):
                    if tile_map[y][x] == "1":
                        tile_x = x * self.tile_size
                        tile_y = y * self.tile_size
                        tile = Tile(vec2(tile_x, tile_y), vec2(self.tile_size))
                        tiles.append(tile)
        except IndexError:
            raise Exception("Provided tilemap size is bigger than expected")

        self.tiles = tiles

    def render(self, win):
        for tile in self.tiles:
            tile.render(win)
