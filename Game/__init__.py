import pygame
import traceback
from .bird import Bird
from .background import draw_background
from .slingshot import Slingshot
from .level_loader import load_level

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

        load_level(1, self)

    def draw(self):
        draw_background(self.win)

        wait = self.slingshot.update()

        if wait and self.won:
            self.rocks = []
            self.birds = []
            self.won = False
            self.slingshot.shot = False

            load_level(self.level, self)

        if self.birds:
            for flap in self.birds:
                flap.move()
                flap.draw(self.win)

        if self.rocks:
            for rock in self.rocks:
                rock.draw(self.win)

    def collisions(self):
        win = True
        if self.birds:
            for flap in self.birds:
                if self.rocks:
                    for rock in self.rocks:
                        if flap.rect.colliderect(rock.rect):
                            flap.dead = True
                if win and not flap.dead:
                    win = False
        return win

    def run(self):
        self.won = False

        try:
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False

                self.draw()

                if self.collisions():
                    self.won = True
                    self.level += 1
                    self.running = False
                    load_level(1, self)

                self.clock.tick(60)
                pygame.display.flip()
        except Exception as e:
            print("An exception occurred:", e)
            pygame.quit()

        traceback.print_exc()
