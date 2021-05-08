# Import the pygame module

import pygame

pygame.init()
W = 1500
H = 1000
FPS = 75
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
finished = False

cat_1_surf = pygame.image.load("cat.png").convert()
cat_1_surf.set_colorkey((24, 255, 24))
cat_1_surf = pygame.transform.scale(cat_1_surf, (cat_1_surf.get_width()//2, cat_1_surf.get_height()//2))
cat_1_mirror = pygame.transform.flip(cat_1_surf, True, False)

x, y = 1320, 0
mx, my = 0, 250
x1, y1 = 1320, 500
mx1, my1 = 0, 750

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    screen.fill((251, 217, 181))
    screen.blit(cat_1_surf, (x, y))
    screen.blit(cat_1_mirror, (mx, my))
    screen.blit(cat_1_surf, (x1, y1))
    screen.blit(cat_1_mirror, (mx1, my1))
    if x > -200:
        x -= 5
    else:
        x = W
    if mx < W:
        mx += 3
    else:
        mx = -200
    if x1 > -200:
        x1 -= 8
    else:
        x1 = W
    if mx1 < W:
        mx1 += 10
    else:
        mx1 = -200

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
