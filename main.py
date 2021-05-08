import pygame
from pygame.draw import *
import math

pygame.init()
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
FPS = 60

pygame.display.update()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
