import random
import pygame
import sys
import pygame_menu

pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
TRANSPARENT = (0, 0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()

zbackground = pygame.image.load("sprites/zbackground.png")
abackground = pygame.image.load("sprites/abackground.png")
up = pygame.image.load("sprites/aup.png")
ax = SCREEN_WIDTH + 70
location = []
interval = SCREEN_WIDTH / 3 + 100
random1, random2 = 0, 0


class FlappyBird(object):
    def __init__(self):
        self.image = pygame.image.load('sprites/flappy_bird.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))

    def draw(self, x, y):
        screen.blit(self.image, (x, y))


def moveB(pos_x, zbackground, abackground):
    pos_x -= 3
    if pos_x < -1400:
        pos_x = 0
    screen.blit(zbackground, [pos_x, 0])
    screen.blit(abackground, [pos_x + 700, 0])
    screen.blit(zbackground, [pos_x + 1400, 0])
    return pos_x


def crashed(score):
    info, _ = info_check()
    df = open('info.txt', 'w')
    df = open('info.txt', 'a')
    for line in info:
        rname = line.split(',')[0]
        rpassword = line.split(',')[1]
        if name.get_value() == rname and password.get_value() == rpassword:
            df.write("{},{},{}".format(name.get_value(), password.get_value(), score))
        else:
            df.write(line + '\n')
    font = pygame.font.SysFont("arial", 40)
    text = font.render("You were crashed by the obstacle.", True, BLACK)
    screen.blit(text, (75, 200))
    pygame.quit()
    sys.exit()


def obstacleMove(dx, dy, speed, dscore):
    for i in range(3):
        if location[i][0] < -70:
            random_y = random.randrange(-400, -100)
            location[i] = [location[(i + 2) % 3][0] + interval, random_y]
        location[i][0] -= speed
        screen.blit(pygame.transform.rotate(up, 180), (location[i][0], location[i][1]))
        screen.blit(up, [location[i][0], location[i][1] + 570])
        if location[i][0] - 10 < dx < location[i][0] + 10:
            if dy > location[i][1] + 495 or dy < location[i][1] + 400:
                crashed(dscore)


def info_check():
    score = 0
    f = open("info.txt", 'r')
    lines = []
    for line in f.readlines():
        lines.append(line)
        rname = line.split(',')[0]
        rpassword = line.split(',')[1]
        if name.get_value() == rname and password.get_value() == rpassword:
            score = int(line.split(',')[2])
            break
        else:
            score = 0
    return lines, score


random_y = random.randrange(-400, -100)
for i in range(3):
    location.append([ax, random_y])
    ax = -75

flappy_bird = FlappyBird()
flappy_birds = []


def start_the_game():
    _, score = info_check()
    x, y = 300, 200
    speed = 1
    check = 0
    pos_x = 0
    weight = 3
    slower_item = 0
    second = 0
    norm = 120
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flappy_bird.draw(x, y)
                    speed = -3
                if event.key == pygame.K_a:
                    weight = 1.5
                    slower_item = 1
                    norm = 240
        if y < -200 or y > 500:
            crashed(score)
        y += speed
        speed += 0.1
        pos_x = moveB(pos_x, abackground, zbackground)
        obstacleMove(x, y, weight, score)
        flappy_bird.draw(x, y)
        pygame.time.delay(10)
        if slower_item:
            second += 1
            if second == 1000:
                second = 0
                slower_item = 0
                weight = 3
                norm = 100
        check += 1
        if check == norm:
            check = 0
            score += 1
        font = pygame.font.SysFont("arial", 25)
        text = font.render("Score: {}".format(score), True, BLACK)
        screen.blit(text, (3, 5))
        pygame.display.update()
        screen.fill(WHITE)
        clock.tick(59)


menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_BLUE)
name = menu.add.text_input('Name: ', default='Player')
password = menu.add.text_input('Password: ', default='1234')
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)