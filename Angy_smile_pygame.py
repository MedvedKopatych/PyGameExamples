import pygame
from pygame.draw import *

pygame.init()

FPS = 60
screen = pygame.display.set_mode((1000, 1000))
screen.fill((153, 153, 255))

def draw_smile(x, y):
    circle(screen, (255, 255, 0), (x, y), 200)

    circle(screen, (255, 0, 0), (x - 75, y - 25), 30)
    circle(screen, (255, 0, 0), (x + 75, y - 25), 30)
    circle(screen, (255, 255, 255), (x - 75, y - 25), 10)
    circle(screen, (255, 255, 255), (x + 75, y - 25), 10)

    rect(screen, (0, 0, 0), (x - 75, y + 100, 150, 20))

    line(screen, (0, 0, 0), (x - 30, y - 40), (x - 200, y - 80), 20)
    line(screen, (0, 0, 0), (x + 30, y - 40), (x + 200, y - 80), 20)



draw_smile(300, 300)
draw_smile(500, 500)
draw_smile(800, 800)

pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
