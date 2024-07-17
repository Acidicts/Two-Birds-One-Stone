import pygame
from .bird import Bird
from .background import draw_background
from .slingshot import Slingshot
from.level_loader import load_level


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Game")

        self.width, self.height = 800, 600
        self.half_width, self.half_height = self.width / 2, self.height / 2

        self.win = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

        self.running = True
        self.level = 1
        self.won = False

        self.slingshot = Slingshot(self)

        self.birds = []
        self.rocks = []

        load_level(self.level, self)

    def draw(self):

        draw_background(self.win)

        wait = self.slingshot.update()

        if wait and self.won:
            self.rocks = []
            self.birds = []
            self.won = False
            self.slingshot.shot = False
            load_level(self.level, self)

        for flap in self.birds:
            flap.move()
            flap.draw(self.win)

        for rock in self.rocks:
            rock.draw(self.win)

    def collisions(self):
        win = True
        for flap in self.birds:
            for rock in self.rocks:
                if flap.rect.colliderect(rock.rect):
                    flap.dead = True
            win = not flap.dead
        return win



    def run(self):
        self.won = False

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()
            self.won = self.collisions()

            if self.won:
                self.level += 1
                self.running = False
                # load_level(self.level, self)

            self.clock.tick(60)
            pygame.display.flip()
