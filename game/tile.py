import pygame
from glm import vec2


class Tile:
    def __init__(self, position: vec2, tile_size: vec2):
        self.pos = position
        self.size = tile_size

        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.size.x, self.size.y)

    def render(self, win):
        pygame.draw.rect(win, (0, 0, 0), self.rect)
