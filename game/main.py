import pygame
from glm import vec2


class Game:
    def __init__(self, win_size: vec2):
        self.win_size = win_size
        self.win = pygame.display.set_mode((int(win_size.x), int(win_size.y)))
        self.background = (255, 255, 255)
        print(win_size)

    def update(self, dt):
        pass

    def render(self):
        pygame.draw.rect(self.win, (255, 0, 0), (self.x, 50, 50, 50))
