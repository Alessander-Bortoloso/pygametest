import sys
import pygame
from settings import *
from level import Level


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Field')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            delta_time = self.clock.tick() / 1000
            self.level.run(delta_time)
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
