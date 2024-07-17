import pygame
import Game.utils as utils

class Bird:
    def __init__(self, x, y, distance, speed, direction, delay=1):
        self.image = utils.load_image("bird_front.png")
        self.image = pygame.transform.scale(self.image, (30, 45))

        self.original_pos = x + 57, y
        self.x, self.y = x + 57, y

        self.rect = pygame.rect.Rect(self.x, self.y, 30, 45)

        self.distance = distance
        self.speed = speed
        self.direction = direction

        self.delay = None
        self.delay_time = delay

    def move(self):
        self.x += self.direction * self.speed
        if self.delay is None:
            if self.x - self.original_pos[0] >= self.distance:
                self.direction *= -1
            elif self.x - self.original_pos[0] <= 0:
                self.direction *= -1
            self.delay = pygame.time.get_ticks()
        else:
            if pygame.time.get_ticks() - self.delay >= self.delay_time * 1000:
                self.delay = None

    def draw(self, screen):
        pygame.draw.line(screen, (0, 0, 0), (100, self.rect.bottom), (700, self.rect.bottom), 3)
        if self.image:
            screen.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 50, 50))
