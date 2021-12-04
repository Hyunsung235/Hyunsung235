import random

def WL(map):
    a = [6, 7, 8, 3, 4, 5, 0, 1, 2, 6, 3, 0, 7, 4, 1, 8, 5, 2, 6, 4, 2, 8, 4, 0]
    wl = 1
    for i in range(8):
        if map[a[i * 3]] == map[a[1 + i * 3]] == map[a[2 + i * 3]]:
            return wl
    wl = 0
    return wl

def PT(map, c):
    printmap(map)
    a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    count = 0
    pc = (input('1 ~ 9 : '))
    for i in range(9):
        if pc == a[i]:
            count = 1
    if count == 1:
        pc = int(pc)
        if map[pc - 1] == a[pc - 1]:
            map[pc - 1] = 'O'
            c = 1
            print(' ')
        else:
            print('there is already O or X')
    else:
        print('1 ~ 9')
    return c


def CT(map):
    map_n = []
    for i in range(9):
        if map[i] != 'X' and map[i] != 'O':
            map_n.append(i + 1)
    cc = map_n[random.randrange(0, len(map_n))]
    map[cc - 1] = 'X'


def printmap(map):
    print(' ----------------')
    print(' ㅣ ' + map[6] + ' ㅣ ' + map[7] + ' ㅣ ' + map[8] + ' ㅣ ')
    print(' ----------------')
    print(' ㅣ ' + map[3] + ' ㅣ ' + map[4] + ' ㅣ ' + map[5] + ' ㅣ ')
    print(' ----------------')
    print(' ㅣ ' + map[0] + ' ㅣ ' + map[1] + ' ㅣ ' + map[2] + ' ㅣ ')
    print(' ----------------')
    print('Player = O, Computer = X')


map = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
n = 5
c = 0

while True:
    c = 0
    while True:
        c = PT(map, c)
        if c == 1:
            break
    print(' ')

    if WL(map) == 1:
        printmap(map)
        print('Player Win')
        break

    n -= 1
    if n == 0:
        printmap(map)
        print('Draw')
        break

    CT(map)

    if WL(map) == 1:
        printmap(map)
        print('Computer Win')
        break

a = input()
