# Import the pygame module

import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1500, 1000))

"""draws ellipse between two points
    A = start point (x,y)
    B = end point (x,y)
    width in pixel
    color (r,g,b)
    line thickness int, if line=0 fill ellipse"""


def draw_ellipse(A, B, width, color, line):

    # point coordinates
    xA, yA = A[0], A[1]
    xB, yB = B[0], B[1]
    # calculate ellipse height, distance between A and B
    AB = math.sqrt((xB - xA)**2 + (yB - yA)**2)

    # difference between corner point coord and ellipse endpoint
    def sp(theta):
        return abs((width / 2 * math.sin(math.radians(theta))))

    def cp(theta):
        return abs((width / 2 * math.cos(math.radians(theta))))

    if xB >= xA and yB < yA:
        # NE quadrant
        theta = math.degrees(math.asin((yA - yB) / AB))
        xP = int(xA - sp(theta))
        yP = int(yB - cp(theta))
    elif xB < xA and yB <= yA:
        # NW
        theta = math.degrees(math.asin((yB - yA) / AB))
        xP = int(xB - sp(theta))
        yP = int(yB - cp(theta))
    elif xB <= xA and yB > yA:
        # SW
        theta = math.degrees(math.asin((yB - yA) / AB))
        xP = int(xB - sp(theta))
        yP = int(yA - cp(theta))
    else:
        # SE
        theta = math.degrees(math.asin((yA - yB) / AB))
        xP = int(xA - sp(theta))
        yP = int(yA - cp(theta))

    # create surface for ellipse !!!!!СЮДА СМОТРЕТЬ ПРО ПОВЕРХНОСТЬ !!!!!
    ellipse_surface = pygame.Surface((AB, width), pygame.SRCALPHA)
    # draw surface onto ellipse
    pygame.draw.ellipse(ellipse_surface, color, (0, 0, AB, width), line)
    # rotate ellipse
    ellipse = pygame.transform.rotate(ellipse_surface, theta)
    # blit ellipse onto screen
    screen.blit(ellipse, (xP, yP))


# Fill the screen with beige
screen.fill((251, 217, 181))

# draw sofa
rect(screen, (48, 213, 200), (0, 700, 800, 300))

# draw TV
rect(screen, (165, 165, 165), (150, 50, 400, 225))
rect(screen, (41, 49, 51), (160, 60, 380, 205))

# draw cat's body
ellipse(screen, (28, 28, 28), (200, 550, 500, 200), 0)

# draw cat's right arm
ellipse(screen, (28, 28, 28), (150, 600, 50, 200), 0)

# draw cat's head
ellipse(screen, (28, 28, 28), (100, 575, 180, 150), 0)

# draw cat's left arm
ellipse(screen, (28, 28, 28), (200, 710, 150, 50), 0)

# draw cat's left leg
circle(screen, (28, 28, 28), (650, 720), 65)
ellipse(screen, (28, 28, 28), (670, 720, 50, 150), 0)

# draw cat's tail
draw_ellipse((620, 590), (900, 850), 40, (28, 28, 28), 0)

# draw right eye
ellipse(screen, (234, 169, 0), (135, 630, 38, 45), 0)
ellipse(screen, (0, 55, 0), (152, 630, 10, 43), 0)
draw_ellipse((143, 635), (155, 645), 5, (255, 255, 255), 0)

# draw left eye
ellipse(screen, (234, 169, 0), (200, 630, 38, 45), 0)
ellipse(screen, (0, 55, 0), (217, 630, 10, 43), 0)
draw_ellipse((210, 635), (222, 645), 5, (255, 255, 255), 0)

# draw nose
polygon(screen, (37, 34, 27), ((178, 675), (195, 675), (186, 685)), 0)
line(screen, (61, 51, 53), (178, 674), (195, 674), 1)
line(screen, (61, 51, 53), (178, 675), (185, 686), 1)
line(screen, (37, 34, 27), (186, 685), (186, 700), 3)

# draw mouth
line(screen, (61, 51, 53), (185, 686), (185, 700), 1)
arc(screen, (61, 51, 53), (166, 692, 20, 15), 3.14, 2*3.14, 1)
arc(screen, (61, 51, 53), (186, 692, 20, 15), 3.14, 2*3.14, 1)

# draw right ear
polygon(screen, (28, 28, 28), ((88, 560), (140, 590), (105, 630)), 0)
polygon(screen, (61, 51, 53), ((94, 568), (130, 590), (108, 617)), 0)

polygon(screen, (28, 28, 28), ((235, 590), (287, 560), (270, 630)), 0)
polygon(screen, (61, 51, 53), ((245, 590), (282, 567), (267, 610)), 0)

# draw mustache
pi = 3.14
arc(screen, (61, 51, 53), (193, 690, 100, 10), pi/8, pi, 1)
arc(screen, (61, 51, 53), (194, 685, 100, 20), pi/5, pi, 1)
arc(screen, (61, 51, 53), (194, 680, 120, 25), pi/3, pi, 1)
arc(screen, (61, 51, 53), (194, 692, 100, 15), pi/2.95, pi, 1)

arc(screen, (61, 51, 53), (78, 695, 100, 10), 0, pi+0.1, 1)
arc(screen, (61, 51, 53), (78, 690, 100, 20), 0, pi-0.5, 1)
arc(screen, (61, 51, 53), (70, 684, 110, 30), 0, pi-0.5, 1)
arc(screen, (61, 51, 53), (68, 680, 110, 30), 0, pi-0.7, 1)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
