import pygame
import sys
import math
import numpy
import time

p1 = {'hp': 100, 'xa': 0, 'ya': 0, 'x': -5000, 'y': 5000, 'a': 'r', 's1': 0, 's2': 50, 'j': False, 's': 'walk', 'c': 1, 'd': False, 'as': None}
p2 = {'hp': 100, 'xa': 0, 'ya': 0, 'x': 5000, 'y': 5000, 'a': 'l', 's1': 0, 's2': 50, 'j': False, 's': 'walk', 'c': 1, 'd': False, 'as': None}

g = 9.8     # 중력 가속도
j = 90     # 점프 가속도
f = 2       # 마찰력
cs = 7      # 좌우 가속도
cs1 = 7
cs2 = 7
cs3 = 17
s2_s = 350   # 스킬 좌우 가속도
s2_j = 200   # 스킬 상하 가속도
max_xa = 20  # 좌우 가속도 최대치
max_1xa = 20 # 좌우 가속도 최대치
max_2xa = 20 # 좌우 가속도 최대치
max_3xa = 50
map_size = [100, 1820, 800] # min x / max x / min y
character_size = [500, 500]
ts_size = [100, 100]
b_size = [125, 125]
ts = 80
tsd = 20
sv = 0.2        #  볼륨 ---------------------------------~~~~!!!!~~~~------------------


p1_tsx = 5000
p2_tsx = 5000
p1_tsy = 5000
p2_tsy = 5000
p1_tsa = 1
p2_tsa = 1
p1_tsi = pygame.transform.scale(pygame.image.load('ts.png'), (ts_size[0], ts_size[1]))
p2_tsi = pygame.transform.scale(pygame.image.load('ts.png'), (ts_size[0], ts_size[1]))
rb = pygame.transform.scale(pygame.image.load('rb.png'), (b_size[0], b_size[1]))
tsb = pygame.transform.scale(pygame.image.load('tsb.jpg'), (b_size[0] - 25, b_size[1] - 25))

background = pygame.image.load('background.png')
hpr = pygame.image.load('redgauge.png')
hpb = pygame.image.load('blackgauge.png')
p1oi = pygame.image.load('p1.png')
p2oi = pygame.image.load('p2.png')
p1i = None
p2i = None

p1we = [x for x in range(9, 19)]
p2we = [13, 12, 11, 10, 9]

p1ae = [19, 20, 21, 22]
p2ae = [21, 22, 23, 24]

p1ge = [68]
p2ge = [5]

p1de = [47, 48, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
p2de = [32, 31, 30, 29, 28, 27]


# 초기화
pygame.init()
pygame.mixer.init()


font = pygame.font.Font(None, 50)
YELLOW = (255, 165, 0)
WHITE = (255, 255, 255)

JK = font.render("J", True, YELLOW)
KK = font.render("K", True, YELLOW)
DK = font.render("2", True, YELLOW)
TK = font.render("3", True, YELLOW)

# 화면 설정 30 30 720
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("I VS I")

# 소리 설정
pygame.mixer.music.load('bgm.mp3')
p1a = pygame.mixer.Sound('p1a.mp3')
p2a = pygame.mixer.Sound('p2a.mp3')
gs = pygame.mixer.Sound('gs.mp3')
ds = pygame.mixer.Sound('ds.mp3')
tss = pygame.mixer.Sound('tss.mp3')
p1a.set_volume(sv)
p2a.set_volume(sv)
gs.set_volume(sv * 0.5)
ds.set_volume(sv * 10)
tss.set_volume(sv)
p1['as'] = p1a
p2['as'] = p2a

pygame.mixer.music.set_volume(sv)

# FPS 설정
FPS = 24   # //-------------------------------------------------------------
clock = pygame.time.Clock()

# 입력 처리


def p1_image(n):
    global p1i
    x = n % 11 if n % 11 != 0 else 1
    y = n // 11 + 1
    p1i = p1oi.subsurface(pygame.Rect((x-1)*100, (y-1)*55, 100, 55))

    if p1['a'] == 'l':
        p1i = pygame.transform.flip(p1i, True, False)

    p1i = pygame.transform.scale(p1i, (character_size[0], character_size[1]))

def p2_image(n):
    global p2i
    x = n % 9 if n % 9 != 0 else 1
    y = n // 9 + 1
    p2i = p2oi.subsurface(pygame.Rect((x-1)*51.875, (y-1)*50, 51.875, 50))

    if p2['a'] == 'r':
        p2i = pygame.transform.flip(p2i, True, False)

    p2i = pygame.transform.scale(p2i, (character_size[0], character_size[1]))

def key_input(keys):
    global p1;  global p2
    global p1_tsa; global p2_tsa
    global p1_tsx; global p2_tsx
    global p1_tsy; global p2_tsy
    global cs, cs1, cs2, cs3
    global max_xa, max_1xa, max_2xa, max_3xa

    if p1['s'] == 'stop' or 'walk':
        if keys[pygame.K_h]:
            p1['s'] = 'attack'
        if keys[pygame.K_s]:
            p1['s'] = 'guard'
        if keys[pygame.K_k] and p1['s1'] == 0 and p1['s'] != 'guard':
            p1_tsa = 1 if p1['a'] == 'r' else -1
            p1_tsx = p1['x']
            p1_tsy = p1['y'] - 50
            p1['s1'] = 100
            tss.play()
        if keys[pygame.K_j] and p1['s2'] > 4 and p1['s'] == 'walk':
            cs1 = cs3
            max_1xa = max_3xa
            p1['s2'] -= 4
        else:
            cs1 = cs
            max_1xa = max_xa
            if p1['s2'] < 100:
                p1['s2'] += 0.5

    if p2['s'] == 'stop' or 'walk':
        if keys[pygame.K_KP_1]:
            p2['s'] = 'attack'
        if keys[pygame.K_DOWN]:
            p2['s'] = 'guard'
        if keys[pygame.K_KP_3] and p2['s1'] == 0 and p2['s'] != 'guard':
            p2_tsa = 1 if p2['a'] == 'r' else -1
            p2_tsx = p2['x']
            p2_tsy = p2['y'] - 50
            p2['s1'] = 100
            tss.play()
        if keys[pygame.K_KP_2] and p2['s2'] >= 4 and p2['s'] == 'walk':
            cs2 = cs3
            max_2xa = max_3xa
            p2['s2'] -= 4
        else:
            cs2 = cs
            max_2xa = max_xa
            if p2['s2'] < 100:
                p2['s2'] += 0.5
    # 좌우 움직임
    if not p1['s'] == 'guard':
        if keys[pygame.K_a]:        p1['xa'] -= cs1;  p1['a'] = 'l'
        if keys[pygame.K_d]:        p1['xa'] += cs1;  p1['a'] = 'r'

    if not p2['s'] == 'guard':
        if keys[pygame.K_LEFT]:     p2['xa'] -= cs2;  p2['a'] = 'l'
        if keys[pygame.K_RIGHT]:    p2['xa'] += cs2;  p2['a'] = 'r'

    # 위 움직임
    if keys[pygame.K_w]  and not p1['j'] and p1['s'] != 'guard':    p1['ya'] = -j;  p1['j'] = True;    p1['y'] -= 100
    if keys[pygame.K_UP] and not p2['j'] and p2['s'] != 'guard':    p2['ya'] = -j;  p2['j'] = True;    p2['y'] -= 100


def character_movement():
    global p1;  global p2
    global p1_tsa; global p2_tsa
    global p1_tsx; global p2_tsx

    # 좌우 가속도 최소치, 최대치 컷
    if p1['xa'] > max_1xa:       p1['xa'] = max_1xa
    if p1['xa'] < -max_1xa:      p1['xa'] = -max_1xa
    if abs(p1['xa']) <= 1:      p1['xa'] = 0
    if p2['xa'] > max_2xa:       p2['xa'] = max_2xa
    if p2['xa'] < -max_2xa:      p2['xa'] = -max_2xa
    if abs(p2['xa']) <= 1:      p2['xa'] = 0

    # 중력과 마찰력
    if not p1['j']:    p1['xa'] -= numpy.sign(p1['xa']) * f
    p1['ya'] += g

    if not p2['j']:    p2['xa'] -= numpy.sign(p2['xa']) * f
    p2['ya'] += g

    # 이동 처리
    p1['x'] += p1['xa'];    p1['y'] += p1['ya']
    p2['x'] += p2['xa'];    p2['y'] += p2['ya']

    p1_tsx += p1_tsa * ts
    p2_tsx += p2_tsa * ts

    if p1['s1'] >= 1:
        p1['s1'] -= 1
    if p2['s1'] >= 1:
        p2['s1'] -= 1

    if p1['hp'] <= 0:
        p1['s'] = 'death'
        p1['d'] = True
        ds.play()

    if p2['hp'] <= 0:
        p2['s'] = 'death'
        p2['d'] = True
        ds.play()

def character_collision():
    global p1_tsi;  global p2_tsi

    # 왼쪽 벽 / 오른쪽 벽 / 바닥
    if p1['x'] <= map_size[0]:  p1['x'] = map_size[0]
    if p1['x'] >= map_size[1]:  p1['x'] = map_size[1]
    if p1['y'] >= map_size[2]:  p1['y'] = map_size[2];   p1['j'] = False

    if p2['x'] <= map_size[0]:  p2['x'] = map_size[0]
    if p2['x'] >= map_size[1]:  p2['x'] = map_size[1]
    if p2['y'] >= map_size[2]:  p2['y'] = map_size[2];   p2['j'] = False



def display_update():
    global p1_tsi; global p2_tsi

    # 체력바 바탕
    screen.blit(hpb, (0, 170))
    screen.blit(hpb, (1170, 170))


    # 체력바 게이지
    screen.blit(hpr, (-31 - 7.30 * (100 - p1['hp']), 170))
    screen.blit(hpr, (1165 + 7.30 * (100 - p2['hp']), 170))

    # 배경
    screen.blit(background, (0, 0))

    # 캐릭터
    p1_image(p1['c'])
    p2_image(p2['c'])
    screen.blit(p1i, (p1['x'] - character_size[0] / 2, p1['y'] - character_size[1] / 2))
    screen.blit(p2i, (p2['x'] - character_size[0] / 2, p2['y'] - character_size[1] / 2))

    # 표창
    screen.blit(p1_tsi, (p1_tsx, p1_tsy))
    screen.blit(p2_tsi, (p2_tsx, p2_tsy))

    # 버튼
    screen.blit(rb, (30, 30))
    screen.blit(font.render(f"{int(p1['s2'] // 1)}", True, YELLOW), (75, 20)) # 버튼의 중앙 y값은 78
    screen.blit(JK, (80, 150)) # 버튼의 중앙 y값은 78

    screen.blit(rb, (1920 - b_size[1] -30, 30))
    screen.blit(font.render(f"{int(p2['s2'] // 1)}", True, YELLOW), (1920 - 105, 20)) # 버튼의 중앙 y값은 78
    screen.blit(DK, (1920 - 105, 150)) # 버튼의 중앙 y값은 78

    if p1['s1'] <= 1:
        screen.blit(tsb, (175, 45))
        screen.blit(KK, (215, 150)) # 버튼의 중앙 y값은 78

    if p2['s1'] <= 1:
        screen.blit(tsb, (1920 - (b_size[0] - 25) - 175, 45))
        screen.blit(TK, (1920 - 235, 150)) # 버튼의 중앙 y값은 78

    if p1['d']:
        screen.blit(font.render("Player 2(bandit) Won!!     Press * key to exit.  >>>  ******", True, WHITE), (700, 400))  # 버튼의 중앙 y값은 78

    if p2['d']:
        screen.blit(font.render("Player 1(brave) Won!!     Press * key to exit.  >>>  ******", True, WHITE), (700, 400))  # 버튼의 중앙 y값은 78
    fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))
    pygame.display.flip()


def animation(p, e):
    if p['c'] in e:
        if e.index(p['c']) + 1 != len(e):
            return e[(e.index(p['c']) + 1)], p['s']
        else:
            if p['s'] == 'death':
                return e[-1], 'death'
            else:
                return 1, 'stop'
    else:
        if p['s'] == 'attack':
            p['as'].play()
        return e[0], p['s']

def p1_animation():
    global p1

    if p1['s'] == 'walk' and p1['xa'] == 0:
        p1['s'] = 'stop'

    if p1['s'] == 'stop' and p1['xa'] != 0:
        p1['s'] = 'walk'

    if p1['s'] == 'stop':
        p1['c'] = 1

    elif p1['s'] == 'walk':
        p1['c'], p1['s'] = animation(p1, p1we)

    elif p1['s'] == 'attack':
        p1['c'], p1['s'] = animation(p1, p1ae)

    elif p1['s'] == 'guard':
        p1['c'], p1['s'] = p1ge[0], 'stop'

    elif p1['s'] == 'death':
        p1['c'], p1['s'] = animation(p1, p1de)


def p2_animation():
    global p2

    if p2['s'] == 'walk' and p2['xa'] == 0:
        p2['s'] = 'stop'

    if p2['s'] == 'stop' and p2['xa'] != 0:
        p2['s'] = 'walk'

    if p2['s'] == 'stop':
        p2['c'] = 1

    elif p2['s'] == 'walk':
        p2['c'], p2['s'] = animation(p2, p2we)

    elif p2['s'] == 'attack':
        p2['c'], p2['s'] = animation(p2, p2ae)

    elif p2['s'] == 'guard':
        p2['c'], p2['s'] = p2ge[0], 'stop'

    elif p2['s'] == 'death':
        p2['c'], p2['s'] = animation(p2, p2de)

def damage(attacker, target, dmg):
    if target['s'] == 'guard':
        if attacker['x'] < target['x']:
            if target['a'] == 'l':
                target['hp'] -= dmg / 10
                gs.play()
                return target
        else:
            if target['a'] == 'r':
                target['hp'] -= dmg / 10
                gs.play()
                return target

    target['hp'] -= dmg
    return target





def judgement():
    global p1, p2
    if p1['s'] == 'attack':
        if p1['y'] - 100 <= p2['y'] <= p1['y'] + 100:
            if p1['a'] == 'l':
                if p2['x'] + 50 <= p1['x'] <= p2['x'] + 250:
                    p2 = damage(p1, p2, 1)
            else:
                if p2['x'] - 50 >= p1['x'] >= p2['x'] - 250:
                    p2 = damage(p1, p2, 1)


    if p2['s'] == 'attack':
        if p2['y'] - 100 <= p1['y'] <= p2['y'] + 100:
            if p2['a'] == 'l':
                if p1['x'] + 50 <= p2['x'] <= p1['x'] + 250:
                    p1 = damage(p2, p1, 1)
            else:
                if p2['x'] + 50 <= p1['x'] <= p2['x'] + 250:
                    p1 = damage(p2, p1, 1)


    if p1_tsx - 10 <= p2['x'] <= p1_tsx + 70 and p1_tsy - 220 <= p2['y'] <= p1_tsy + 200:
        p2 = damage(p1, p2, tsd)

    if p2_tsx + 10 <= p1['x'] <= p2_tsx + 90 and p2_tsy - 220 <= p1['y'] <= p2_tsy + 200:
        p1 = damage(p2, p1, tsd)






def main():

    for i in range(1, 4):
        screen.blit(pygame.transform.scale(pygame.image.load(f'{str(4 - i) * 3}.png'), (1920, 1080)), (0, 0))
        screen.blit(pygame.transform.scale(pygame.image.load(f'444.png'), (800, 300)), (600, 0))
        pygame.display.flip()
        time.sleep(1.5)

    pygame.mixer.music.play(loops=-1)
    while True:
        if not (p1['d'] or p2['d']):
            key_input(pygame.key.get_pressed())
            character_movement()
        character_collision()
        judgement()
        p1_animation()
        p2_animation()
        display_update()


        clock.tick(FPS)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 창 닫기 이벤트
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:  # 키 눌림 이벤트
                if event.unicode == '*':  # '*' 키 확인
                    pygame.quit()
                    exit()

if __name__ == "__main__":
    main()
