import pygame
from glm import vec2

from .level import Level


class Game:
    def __init__(self, win_size: vec2):
        self.win_size = win_size
        self.win = pygame.display.set_mode((int(win_size.x), int(win_size.y)))
        self.background = (255, 255, 255)
        print(win_size)

        self.l = Level(self.win_size)
        self.l.build_level()

    def update(self, dt):
        pass

    def render(self):
        self.l.render(self.win)
