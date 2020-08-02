import pygame
from glm import vec2

from game.main import Game

def main():
    game = Game(vec2(800, 600))
    fps = 60
    clock = pygame.time.Clock()
    while True:
        dt = clock.tick(fps) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        game.update(dt)
        game.win.fill(game.background)
        game.render()
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()