import pygame
from .bird import Bird


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Game")

        self.width, self.height = 800, 600
        self.half_width, self.half_height = self.width / 2, self.height / 2

        self.win = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

        self.running = True

        self.birds = []

    def draw(self):
        self.win.fill((255, 255, 255))

        for flap in self.birds:
            flap.move()
            flap.draw(self.win)

        pygame.draw.line(self.win,  (193, 154, 107), (92, 100), (92, 600), 15)
        pygame.draw.line(self.win, (193, 154, 107), (707, 100), (707, 600), 15)
        pygame.draw.line(self.win, (193, 154, 107), (92, 100), (50, 50), 15)
        pygame.draw.line(self.win, (193, 154, 107), (707, 100), (750, 50), 15)
        pygame.draw.line(self.win, (193, 154, 107), (50, 50), (750, 50), 15)
        pygame.draw.circle(self.win, (193, 154, 107), (92, 100), 7.5, 15)
        pygame.draw.circle(self.win, (193, 154, 107), (707, 100), 7.5, 15)

    def run(self):
        self.birds.append(Bird(100, 100, 100, 1, 1))

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()

            self.clock.tick(60)
            pygame.display.flip()
