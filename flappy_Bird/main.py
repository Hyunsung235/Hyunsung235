import pygame
import sys
import random

x = 0
cooldown = 0
background = pygame.image.load("zbackground.png")
down = pygame.image.load("adown.png")
up = pygame.image.load("aup.png")
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
pygame.display.set_caption("Simple PyGame Example")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pos_x = 0
pos_y = 0
location = []
interval = SCREEN_WIDTH / 3

clock = pygame.time.Clock()
random1, random2 = 0, 0
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key_event = pygame.key.get_pressed()

    pos_x -= 2.5
    if pos_x < -700:
        pos_x = 0

    screen.blit(background, [pos_x, 0])
    screen.blit(background, [pos_x + 700, 0])

    for i in range(1,4):
        x = SCREEN_WIDTH + interval * i
        random_y = random.randrange(-400, -100)
        location.append([x, random_y])
    for i in range(3):
        if location[i][0] < 0:
            location[i][0] = location[(i + 2) % 3][0] + interval

        location[i][0] -= 5
        screen.blit(down, [location[i][0], location[i][1]])
        screen.blit(up, [location[i][0], location[i][1] + 570])

        pygame.display.update()





#    x -= 5
#    if x < 0:
#        for i in range(3):
#            x = 800 + interval * i
#            random_y = random.randrange(-400, -100)
#            location.append([x, random_y])
#    for i in range(3):
#        if location[i][0] < 0:
#            location[i][0] = 800 + location[i + 2][0]
#        screen.blit(down, [location[i][0], location[i][1]])
#        screen.blit(up, [location[i][0], location[i][1] + 570])
#        location[i][0] -= 5