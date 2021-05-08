# Import the pygame module

import pygame
from pygame.draw import *
import pygame.gfxdraw
import pygame.locals
from pygame.locals import *





pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 1000))


# Fill the screen with beige
screen.fill((251, 217, 181))

# draw sofa
rect(screen, (48, 213, 200), (0, 700, 800, 300))

#draw TV
rect(screen, (165, 165, 165), (150, 50, 400, 225))
rect(screen, (41, 49, 51), (160, 60, 380, 205))

# draw cat's body
def rotate(body, angle):
    body = ellipse(screen, (28, 28, 28), (200, 550, 500, 200), 0)


# draw cat's right arm
'''ellipse(screen, (28, 28, 28), (150, 600, 50, 200), 0)

# draw cat's head
ellipse(screen, (28, 28, 28), (100, 575, 180, 150), 0)

# draw cat's left arm
ellipse(screen, (28, 28, 28), (200, 710, 150, 50), 0)

# draw cat's left leg
circle(screen, (28, 28, 28), (650, 720), 65)
ellipse(screen, (28, 28, 28), (670, 720, 50, 150), 0)

# draw cat's tail
pygame.gfxdraw.filled_ellipse(screen, 800, 700, 1000, 20, (28, 28 , 28))'''
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()