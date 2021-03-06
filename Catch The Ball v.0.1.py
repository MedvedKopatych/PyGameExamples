import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1.8
screen = pygame.display.set_mode((1200, 900))
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
SCORES = 0

font = pygame.font.SysFont('arial', 40)
sc_text = font.render('SCORES:', 1, RED, BLACK)
SCORES_pos = sc_text.get_rect(center=(520, 40))

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)




def new_ball():
    '''рисует новый шарик '''
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 800)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


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
            else:
                print('Missed')
        elif event.type == pygame.MOUSEBUTTONUP:
            pygame.display.update()
            screen.fill(BLACK)
    new_ball()

    screen.blit(sc_text, SCORES_pos)
    draw_text(screen, str(SCORES), 40, 620, 18)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
