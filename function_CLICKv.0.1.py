import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

f_sys = pygame.font.SysFont('arial', 12)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
SCORES = 0

sc_text = f_sys.render('SCORES', 1, RED, YELLOW)
SCORES_pos = sc_text.get_rect(center=(600, 0))


def new_ball():
    '''рисует новый шарик '''
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def click(event):
    print(x, y, r)

pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            evt_x = pos[0]
            evt_y = pos[1]
            if (evt_x - x)**2 + (evt_y - y)**2 <= r**2:
                SCORES += 1
                print('SCORES:', SCORES)
                screen.fill(BLACK)
            else:
                print('Missed')
    new_ball()

    screen.blit(sc_text, SCORES_pos)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
