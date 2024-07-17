import pygame
from .utils import load_image


class Bird:
    def __init__(self, x, y, distance, speed, direction, delay=1):
        image = load_image("bird_side.png")

        self.images = {
            "front": pygame.transform.scale(load_image("bird_front.png"), (30, 45)),
            "right": pygame.transform.scale(pygame.transform.flip(image, True, False), (33, 45)),
            "left": pygame.transform.scale(load_image("bird_side.png"), (33, 45))
        }

        self.image = self.images["front"]
        self.dead = False

        self.original_pos = x + 57, y
        self.x, self.y = x + 57, y

        self.rect = pygame.rect.Rect(self.x, self.y, 30, 45)

        self.distance = distance
        self.speed = speed
        self.direction = direction

        self.delay = 0
        self.delay_time = delay

    def move(self):
        if self.delay == 0:

            self.x += self.speed * self.direction
            self.image = self.images["right"] if self.direction == 1 else self.images["left"]

            if self.x - self.original_pos[0] >= self.distance:
                self.direction *= -1
                self.delay = pygame.time.get_ticks()

            elif self.x - self.original_pos[0] <= 0:
                self.direction *= -1
                self.delay = pygame.time.get_ticks()

        elif pygame.time.get_ticks() - self.delay >= self.delay_time * 1000:
            self.delay = 0
        else:
            self.image = self.images["front"]

    def draw(self, screen):
        pygame.draw.line(screen, (0, 0, 0), (100, self.rect.bottom), (700, self.rect.bottom), 3)

        if self.image and not self.dead:
            screen.blit(self.image, (self.x, self.y))
