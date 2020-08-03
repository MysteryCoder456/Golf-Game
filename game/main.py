import pygame
from glm import vec2

from .tile import Tile


class Game:
    def __init__(self, win_size: vec2):
        self.win_size = win_size
        self.win = pygame.display.set_mode((int(win_size.x), int(win_size.y)))
        self.background = (255, 255, 255)
        print(win_size)

        self.t = Tile(vec2(50, 50), vec2(34, 34))

    def update(self, dt):
        pass

    def render(self):
        self.t.render(self.win)
