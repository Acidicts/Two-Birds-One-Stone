import pygame
from Game.utils import load_image


class Slingshot:
    def __init__(self, game):
        self.game = game
        self.image = pygame.transform.scale(load_image("slingshot.png"), (60, 60))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0, 560)
        self.shot = False

        self.wait = 0

    def draw(self):
        self.game.win.blit(self.image, self.rect)

    def update(self):
        self.events()
        self.draw()

        if self.shot and pygame.time.get_ticks() - self.wait > 3000:
            return True

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > self.game.width - 60:
            self.rect.right = self.game.width - 60

    def events(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and not self.shot:
            self.game.rocks.append(Rock(self.rect.centerx, self.rect.centery - 20))
            self.shot = True
            self.wait = pygame.time.get_ticks()

        if keys[pygame.K_LEFT]:
            self.rect.x -= 10
        if keys[pygame.K_RIGHT]:
            self.rect.x += 10


class Rock:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(load_image("rock.png"), (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, screen):
        self.rect.y -= 10
        screen.blit(self.image, self.rect)
