import pygame


def draw_background(win):
    win.fill(pygame.Color("skyblue"))

    pygame.draw.line(win,  (193, 154, 107), (92, 100), (92, 600), 15)
    pygame.draw.line(win, (193, 154, 107), (707, 100), (707, 600), 15)
    pygame.draw.line(win, (193, 154, 107), (92, 100), (50, 50), 15)
    pygame.draw.line(win, (193, 154, 107), (707, 100), (750, 50), 15)
    pygame.draw.circle(win, (193, 154, 107), (50, 50), 7.5)
    pygame.draw.circle(win, (193, 154, 107), (750, 50), 7.5)
    pygame.draw.circle(win, (193, 154, 107), (92, 100), 7.5)
    pygame.draw.circle(win, (193, 154, 107), (707, 100), 7.5)

    pygame.draw.rect(win, pygame.Color("darkgreen"), (0, 550, 800, 600))
