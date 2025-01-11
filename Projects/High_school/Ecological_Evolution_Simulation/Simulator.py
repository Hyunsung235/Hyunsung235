import pygame
import random
import math
import sys

# 유전자 각각의 정보 : L : 왼쪽으로 회전, R : 오른쪽으로 회전, G : 직진, S : 한 턴 쉼, F : 여우의 반대방향 바라보기, W : 물가 바라보기, C : 당근 바라보기, B : 수풀 바라보기
# 토끼 개채 형식 : {gene : 유전자, state : char, turn : 수치, position : [x, y, a]}
# 여우 개채 형식 : [x, y, a, target, turn] 각각 x, y좌표, 각도, 쫒는 대상, 쫒은 턴
# 유전자 형식 : (갈증 내성 수치)_(굶주림 내성 수치)_(속도)_(시아)_(위험시 유전자)_(갈증시 유전자)_(굶주림시 유전자)_(안전시 유전자)
# 상태 형식 : [현 상태, 갈증 수치, 굶주림 수치]
# 토끼의 시아와 속도는 루트해서 사용

# danger gene 생성 값들
danger_gene_maker = 'LRFFFSSSGGGGG'
thirsty_gene_maker = "LRWSSSGGG"
hungry_gene_maker = "LRCSSSGGG"
safe_gene_maker = "LRBSSSGGG"

# 토끼가 방향 유전자 하나로 움직일 각도
move_angle = 15

# 토끼의 유전자 최대길이
rabbit_max_gene_length = 50

# 토끼의 속도계수
rabbit_speed_coefficient = 3

# 토끼의 시아계수
rabbit_sight_coefficient = 0.1

# 토끼의 상태변경 기준 계수(갈증, 배고픔 수치)
rabbit_state_standard = 0.5

# 토끼의 턴당 갈증 감소치
rabbit_thirsty = 0.1

# 토끼의 턴당 배고픔 감소치
rabbit_hungry = 0.05

# 토끼의 사망 판정기준(여우와의 거리)
rabbit_death = 3

# 여우의 속도
fox_speed = 6

# 여우의 시아값
fox_sight = 400

# 여우가 토끼를 쫒는 턴
fox_turn_limit = 150

# 각각 그대로 유전, 능력치 돌연변이, 유전자 돌연변이, 유전자 단위 교차의 비율(총합이 1을 초과해도 되지만, 각각의 수치가 1을 초과할 수는 없음)
same, change1, change2, mix1 = 0.1, 0.05, 0.05, 0.55

# 좋은 유전자의 비율
goodgene = 0.8

# 위치값들 ((x1, x2), (y1, y2)) 이면 x1 ~ x2, y1 ~ y2 사이 범위를 위치로 지정(판정)
bush = ((105, 735), (105, 415))
carrot = ((40, 210), (880, 1050))
river = ((1345, 1920), (0, 1080))
rabbit_summon_range = ((105, 735), (105, 415))
fox_summon_range = ((860, 1060), (440, 640))


# 완성
# pygame 실행을 위한 초기화 함수
def setpygame():
    global screen
    global background
    global fox_sprite
    global rabbit_sprite

    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption('Simulation')
    background = pygame.image.load("sprites/background.png")
    fox_sprite = pygame.transform.scale(pygame.image.load("sprites/fox.png"), (90, 90))
    rabbit_sprite = pygame.transform.scale(pygame.image.load("sprites/rabbit.png"), (90, 90))


# 완성
# 토끼 개체 생성및 초기화 함수, gene이 들어온 경우, 유전자 초기값을 gene값으로 설정
def summon_rabbit(gene=None):
    # 개체 형식 생성
    index = {}

    # 유전자가 입력되지 않은 경우 유전자를 초기화함
    if gene == None:
        # 개체 유전자 생성
        # _로 구분, 순서대로 dehydration, starvation, speed, sight, danger_gene, thirsty_gene, hungry_gene, safe_gene
        dehydration = random.randrange(1, 101)
        starvation = random.randrange(1, 101)
        speed = random.randrange(1, 101)
        sight = random.randrange(1, 101)

        index['gene'] = '{}_{}_{}_{}_S_S_S_S'.format(dehydration, starvation, speed, sight)

    # 유전자가 입력된 경우 입력된 유전자를 초기값으로 설정
    else:
        index['gene'] = gene

        # 갈증과 허기를 최대치로 맞춰주기 위함
        dehydration, starvation = map(int, gene.split('_')[0:2])

    # 토끼의 상태 초기화, 굶주림과 갈증은 최대값으로 설정(0이 될 시 개체 사망)
    index['state'] = ['safe', dehydration, starvation]

    # 토끼의 유전자 해석순서 초기화
    index['turn'] = 0

    # 토끼의 위치 초기화
    a = 0
    x = random.randrange(rabbit_summon_range[0][0], rabbit_summon_range[0][1])
    y = random.randrange(rabbit_summon_range[1][0], rabbit_summon_range[1][1])
    index['position'] = [x, y, a]

    return index


# 완성
# 여우 개체 생성 및 초기화 함수
def summon_fox():
    # 개체 형식 생성
    index = []

    # 여우의 위치 초기화
    a = 0
    x = random.randrange(fox_summon_range[0][0], fox_summon_range[0][1])
    y = random.randrange(fox_summon_range[1][0], fox_summon_range[1][1])
    target = 0
    turn = 0

    # 여우 개체 형성
    index = [x, y, a, target, turn]

    return index


# 완성
# 새로운 유전자를 하나 추가함
def make_gene(state=''):
    if state == 'danger':
        return danger_gene_maker[random.randrange(len(danger_gene_maker))]
    elif state == 'thirsty':
        return thirsty_gene_maker[random.randrange(len(thirsty_gene_maker))]
    elif state == 'hungry':
        return hungry_gene_maker[random.randrange(len(hungry_gene_maker))]
    elif state == 'safe':
        return safe_gene_maker[random.randrange(len(safe_gene_maker))]
    else:
        # 기본값, 돌연변이에 사용
        return "LRFWCBSSSSSSGGGGGG"[random.randrange(18)]


# 완성
# 살아남은 토끼의 유전자들을 합치거나, 섞거나, 돌연변이를 일으킴
def generate_gene(gene):
    if math.ceil(len(gene) * goodgene) < len(gene):
        good_gene = gene[0:math.ceil(len(gene) * goodgene)]
    else:
        good_gene = gene

    # 리턴할 유전자
    index = []

    # 그대로, 능력치 돌연변이, 이동 유전자 돌연변이, 유전자 단위 교차, 유전자 내부의 교차 의 비율 :20%, 10%, 20%, 20%, 10%,     20%은 랜덤생성

    # 그대로
    for i in range(math.ceil(len(gene) * same)):
        index.append(good_gene[i])

    # 능력치 돌연변이
    for i in range(math.ceil(len(gene) * change1)):
        current_gene = good_gene[random.randrange(0, len(good_gene))]
        dehydration, starvation, speed, sight, danger_gene, thirsty_gene, hungry_gene, safe_gene = current_gene.split(
            "_")

        # 수치의 변경값
        n = random.randrange(0, 101)

        # 변경할 수치를 결정하는 값
        m = random.randrange(0, 3)

        if m == 0:
            dehydration = n
        elif m == 1:
            starvation = n
        elif m == 2:
            speed = n
        else:
            sight = n

        index.append('{}_{}_{}_{}_{}_{}_{}_{}'.format(dehydration, starvation, speed, sight, danger_gene, thirsty_gene,
                                                      hungry_gene, safe_gene))

    # 이동 유전자 돌연변이
    for i in range(math.ceil(len(gene) * change2)):
        current_gene = good_gene[random.randrange(0, len(good_gene))]
        dehydration, starvation, speed, sight, danger_gene, thirsty_gene, hungry_gene, safe_gene = current_gene.split(
            "_")

        danger_gene_list = list(danger_gene)
        thirsty_gene_list = list(thirsty_gene)
        hungry_gene_list = list(hungry_gene)
        safe_gene_list = list(safe_gene)

        for _ in range(random.randrange(1, 10)):
            danger_gene_list[random.randrange(0, len(danger_gene_list))] = make_gene()
            thirsty_gene_list[random.randrange(0, len(thirsty_gene_list))] = make_gene()
            hungry_gene_list[random.randrange(0, len(hungry_gene_list))] = make_gene()
            safe_gene_list[random.randrange(0, len(safe_gene_list))] = make_gene()

        danger_gene = ''.join(danger_gene_list)
        thirsty_gene = ''.join(thirsty_gene_list)
        hungry_gene = ''.join(hungry_gene_list)
        safe_gene = ''.join(safe_gene_list)

        index.append('{}_{}_{}_{}_{}_{}_{}_{}'.format(dehydration, starvation, speed, sight, danger_gene, thirsty_gene,
                                                      hungry_gene, safe_gene))

    # 유전자 단위 교차
    for _ in range(math.ceil(len(gene) * mix1)):
        gene1, gene2 = good_gene[random.randrange(0, len(good_gene))], good_gene[random.randrange(0, len(good_gene))]
        dehydration1, starvation1, speed1, sight1, danger_gene1, thirsty_gene1, hungry_gene1, safe_gene1 = gene1.split(
            "_")
        dehydration2, starvation2, speed2, sight2, danger_gene2, thirsty_gene2, hungry_gene2, safe_gene2 = gene2.split(
            "_")

        # 두개의 값중 하나를 랜덤선택해 더해줌
        index.append('{}_{}_{}_{}_{}_{}_{}_{}'.format(
            random.choice((dehydration1, dehydration2)),
            random.choice((starvation1, starvation2)),
            random.choice((speed1, speed2)),
            random.choice((sight1, sight2)),
            random.choice((danger_gene1, danger_gene2)),
            random.choice((thirsty_gene1, thirsty_gene2)),
            random.choice((hungry_gene1, hungry_gene2)),
            random.choice((safe_gene1, safe_gene2))
        ))

    return index


# 완성
# 기준 위치(character)과 캐릭터들의 값들(others)을 받아, 가장 가까운 캐릭터와 거리를 계산해, 기준보다 가까우면 True와 그 캐릭터의 위치, 아니면 False와 [0, 0]를 리턴함, check는 용도를 나타내는 값으로, True이면 리턴값에 위치값이 없고, False면 리턴값에 위치값이 있다
def detection(character, others, reference, check):
    # 최소거리 distance 초기화
    least_distance = float('inf')

    # 최소거리인 객체의 위치값 least_x, least_y
    least_x, least_y = 0, 0

    # 모든 개체에 대해서 계산
    for i in others:

        # 특정한 개체의 위치값 x, y

        # 토끼의 경우
        if isinstance(i, dict):
            x = i['position'][0]
            y = i['position'][1]

        # 여우의 경우
        else:
            x = i[0]
            y = i[1]

        # 개체가 풀숲 안에 있다면 처리하지 않음
        if bush[0][0] <= x <= bush[0][1] and bush[1][0] <= y <= bush[1][1]:
            continue

        # 특정한 개체에 대한 거리 r
        r = math.sqrt((character[0] - x) ** 2 + (character[1] - y) ** 2)

        # 특정한 개체와의 거리가 최소거리 미만이면 경신함
        if least_distance > r:
            least_distance = r
            least_x, least_y = x, y

            # 단순 확인용이면 바로 리턴
            if check and least_distance < reference:
                return True

    # 단순 확인용인 경우 찾지 못했으므로 False
    if check:
        return False

    else:
        # 최소거리가 기준거리 미만일 경우 True와 가장 가까운 개체의 위치값 리턴
        if least_distance < reference:
            return (True, (least_x, least_y))

        # 최소거리가 기준거리 이상인 경우
        else:
            return (False, (least_x, least_y))


# 완성
# 토끼의 유전자를 해석함, 해석이 끝난 뒤 토끼 개체 형식으로 리턴함
def rabbit_movement(character, fox):
    # 여러 상수들을 나눠담음

    dehydration, starvation, speed, sight, danger_gene, thirsty_gene, hungry_gene, safe_gene = character["gene"].split(
        "_")
    dehydration, starvation, speed, sight = map(int, (dehydration, starvation, speed, sight))

    # --------------------------------------------------------------------
    # 상태를 변경

    exist, least_fox = detection(character["position"], fox, sight ** 2 * rabbit_sight_coefficient, False)

    if exist:
        new_state = 'danger'
        current_gene = danger_gene

    elif character["state"][1] < math.ceil(dehydration * rabbit_state_standard):
        new_state = 'thirsty'
        current_gene = thirsty_gene

    elif character["state"][2] < math.ceil(starvation * rabbit_state_standard):
        new_state = 'hungry'
        current_gene = hungry_gene

    else:
        new_state = 'safe'
        current_gene = safe_gene

    # --------------------------------------------------------------------
    # 상태가 같으면 유전자 해석 순서를 동일하게, 다르면 처음부터 해석

    if character['state'][0] == new_state:
        character['turn'] += 1

    else:
        character['state'][0] = new_state
        character['turn'] = 0

    # --------------------------------------------------------------------
    # 만약 해석할 유전자가 없다면, 랜덤하게 생성

    if len(current_gene) <= character["turn"]:

        # 유전자가 너무 길다면 처음부터 시작
        if len(current_gene) >= rabbit_max_gene_length:
            character["turn"] = 0

        else:
            current_gene += make_gene(character['state'][0])

            # 기존에 유전자에도 적용(저장용)
            if character['state'][0] == 'danger':
                danger_gene = current_gene

            elif character['state'][0] == 'thirsty':
                thirsty_gene = current_gene

            elif character['state'][0] == 'hungry':
                hungry_gene = current_gene

            else:
                safe_gene = current_gene

            character['gene'] = '{}_{}_{}_{}_{}_{}_{}_{}'.format(dehydration, starvation, speed, sight, danger_gene,
                                                                 thirsty_gene, hungry_gene, safe_gene)

    # --------------------------------------------------------------------
    # 유전자를 해석해 움직임

    # 반시계방향 회전
    if current_gene[character["turn"]] == 'L':
        character['position'][2] += move_angle

    # 시계방향 회전
    elif current_gene[character["turn"]] == 'R':
        character['position'][2] -= move_angle

    # 가장 가까운 여우를 피하는 방향
    elif current_gene[character["turn"]] == 'F':
        character["position"][2] = math.degrees(
            math.atan2(least_fox[0] - character["position"][0], least_fox[1] - character["position"][1]))

    # 강 방향
    elif current_gene[character["turn"]] == 'W':
        character["position"][2] = math.degrees(math.atan2((river[0][0] + river[0][1]) / 2 - character["position"][0],
                                                           (river[1][0] + river[1][1]) / 2 - character["position"][
                                                               1])) + 180

    # 당근 방향
    elif current_gene[character["turn"]] == 'C':
        character["position"][2] = math.degrees(math.atan2((carrot[0][0] + carrot[0][1]) / 2 - character["position"][0],
                                                           (carrot[1][0] + carrot[1][1]) / 2 - character["position"][
                                                               1])) + 180

    # 수풀 방향
    elif current_gene[character["turn"]] == 'B':
        character["position"][2] = math.degrees(math.atan2((bush[0][0] + bush[0][1]) / 2 - character["position"][0],
                                                           (bush[1][0] + bush[1][1]) / 2 - character["position"][
                                                               1])) + 180

    # 직진
    elif current_gene[character["turn"]] == 'G':
        character['position'][0] -= math.sqrt(speed) * math.sin(
            math.radians(character['position'][2])) * rabbit_speed_coefficient
        character['position'][1] -= math.sqrt(speed) * math.cos(
            math.radians(character['position'][2])) * rabbit_speed_coefficient

        # 배경 밖을 못 나가게 설정
        if 0 > character['position'][0]:
            character['position'][0] = 50
        if 1920 < character['position'][0]:
            character['position'][0] = 1830
        if 0 > character['position'][1]:
            character['position'][1] = 50
        if 1080 < character['position'][1]:
            character['position'][1] = 1030

    # 한 턴 쉼. transcription = 'S'인 경우.
    else:
        pass

    # --------------------------------------------------------------------
    # 토끼의 위치가 물이나 당근 범위 내라면 알맞는 처리를 함

    if river[0][0] <= character['position'][0] <= river[0][1] and river[1][0] <= character['position'][1] <= river[1][
        1]:
        character['state'][1] = dehydration
    elif carrot[0][0] <= character['position'][0] <= carrot[0][1] and carrot[1][0] <= character['position'][1] <= \
            carrot[1][1]:
        character['state'][2] = starvation

    # --------------------------------------------------------------------
    # 계산을 끝낸 character 리턴

    return character


# ---------------------------------------------------------------------------------------
# 미완성
# 여우 한 개체의 움직임, 움직임이 끝난 여우 개체를 리스트로 반환함
def fox_movement(fox, rabbit):
    # 가장 가까운 토끼의 위치를 파악함
    exist, least_rabbit = detection(fox, rabbit, fox_sight, False)
    if exist:

        # 최단거리인 토끼개체를 찾음
        for i in range(len(rabbit)):
            if (rabbit[i]['position'][0], rabbit[i]['position'][1]) == least_rabbit:
                if fox[3] == i:
                    fox[4] += 1
                else:
                    fox[3] = i
                    fox[4] = 0
                break

        # 너무 오래 쫒으면 포기
        if fox[4] < fox_turn_limit:
            fox[2] = math.atan2(least_rabbit[0] - fox[0], least_rabbit[1] - fox[1])

        fox[0] += fox_speed * math.sin(fox[2])
        fox[1] += fox_speed * math.cos(fox[2])

    else:
        # 현재는 토끼를 발견 못했을땐 멈춤
        pass

    # 이동
    return fox


# 완성
# 시뮬레이션을 한 번 돌림, 가공된 유전자를 받은 경우엔, 받은 유전자를 토대로 토끼를 생성함, 늦게 죽을수록 앞에 오는 리스트를 반환, 살아남을 경우 거의 랜덤으로 앞에 옴
def simulation_progress(turn_limit, rabbit_population, fox_population, printscreen, gene=[]):
    # 토끼와 여우의 개체수를 확보함
    fox = []
    rabbit = []
    n = 0

    while n < rabbit_population:
        if n < len(gene):
            rabbit.append(summon_rabbit(gene[n]))
        else:
            rabbit.append(summon_rabbit())

        n = len(rabbit)

    while len(fox) < fox_population:
        fox.append(summon_fox())

    # 시뮬레이션
    turn = 0

    # 사망한 토끼, 늦게 죽은 개체의 유전자가 앞에 옴
    death = []

    # 시뮬레이션
    while len(rabbit) > 0 and turn < turn_limit:

        # 턴을 한턴 올려줌
        turn += 1

        # 토끼들과 여우들이 움직임
        for i in range(len(rabbit)):
            rabbit[i] = rabbit_movement(rabbit[i], fox)
            if printscreen:
                sprite = pygame.transform.rotate(rabbit_sprite, rabbit[i]['position'][2])
                screen.blit(sprite, sprite.get_rect(center=(rabbit[i]['position'][0], rabbit[i]['position'][1])))
        for i in range(len(fox)):
            fox[i] = fox_movement(fox[i], rabbit)
            if printscreen:
                sprite = pygame.transform.rotate(fox_sprite, fox[i][2] * 180 / math.pi - 90)
                screen.blit(sprite, sprite.get_rect(center=(fox[i][0], fox[i][1])))

        # 토끼의 상태변화(갈증, 배고픔 수치 감소)와 사망처리를 하고 사망판정된 토끼를 pop_list에 담음
        pop_list = []
        for r in rabbit:
            # 상태변화
            r["state"][1] -= rabbit_thirsty
            r["state"][2] -= rabbit_hungry

            # 갈증이나, 배고픔 수치가 0이하가 되면 사망처리
            if r["state"][1] <= 0 or r["state"][2] <= 0:
                pop_list.append(r)
                death.insert(0, r['gene'])

            # 토끼와 가장 가까운 여우의 위치가 특정 값 이하일 경우 사망처리
            elif detection(r['position'], fox, rabbit_death, True):
                pop_list.append(r)
                death.insert(0, r['gene'])

        # 사망판정된 토끼를 토끼 리스트에서 솎아냄
        alive_rabbit = []
        for r in rabbit:
            if not r in pop_list:
                alive_rabbit.append(r)

        rabbit = alive_rabbit

        # 배경처리
        if printscreen:
            pygame.display.update()
            screen.blit(background, (0, 0))
            pygame.event.get()


    return death


# 루프
gene = []
while True:

    print('-------------------------------------------------------')
    turn_limit = int(input('시뮬레이션의 최대 턴수 : '))
    rabbit_population = int(input('토끼의 개체수 : '))
    fox_population = int(input('여우의 개체수 : '))
    printscreen = (input('시뮬레이션의 화면 출력 여부(T/F) : '))
    repeat = int(input('반복 횟수 : '))
    gene_append = input('추가할 유전자(없다면 N) : ')

    if printscreen == 'T':
        printscreen = True
    else:
        printscreen = False

    if printscreen:
        setpygame()

    for i in range(repeat):
        if not gene_append.isdigit() and gene_append != 'N':
            gene.append(gene_append)

        death = simulation_progress(turn_limit, rabbit_population, fox_population, printscreen, gene)
        if death == None:
            death = []
        gene = generate_gene(death)

        if gene == None:
            gene = []

        if len(death) == 0:
            print('제 {}회, 최적화된 유전자 : {}'.format(i + 1, '모든 개체 생존'))
        else:
            print('제 {}회, 최적화된 유전자 : {}'.format(i + 1, death[0]))

    if printscreen:
        pygame.quit()