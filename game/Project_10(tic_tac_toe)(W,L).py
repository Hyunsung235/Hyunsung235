#print(str + str)

import random

def WL(pc,OX,map):
    for i in range(3):
        if map[3 * i] == OX and map[3 * i + 1] == OX and map[3 * i + 2] == OX:
            pc = 1
            return (pc)
        if map[6 + i] == OX and map[3 + i] == OX and map[0 + i] == OX:
            pc = 1
            return (pc)
    if map[0] == OX and map[4] == OX and map[8] == OX:
        pc = 1
        return (pc)
    elif map[2] == OX and map[4] == OX and map[6] == OX:
        pc = 1
        return (pc)
    return(pc)

def CT(map):
    map_n = []
    for i in range(9):
        if map[i] != 'X' and map[i] != 'O':
            map_n.append(i + 1)
    cc = map_n[random.randrange(0, len(map_n))]
    return cc







map = ['1','2','3','4','5','6','7','8','9']
p_s = 0
p_w = 0
map_n = []
pc = 0
cc = 0
n = 5

while True:
    print(' ----------------')
    print(' ㅣ ' + map[6] + ' ㅣ ' + map[7] + ' ㅣ ' + map[8] + ' ㅣ ')
    print(' ----------------')
    print(' ㅣ ' + map[3] + ' ㅣ ' + map[4] + ' ㅣ ' + map[5] + ' ㅣ ')
    print(' ----------------')
    print(' ㅣ ' + map[0] + ' ㅣ ' + map[1] + ' ㅣ ' + map[2] + ' ㅣ ')
    print(' ----------------')
    print('Player = O, Computer = X')
    pc = int(input('1 ~ 9 : '))

    map[pc - 1] = 'O'

    p_w = WL(p_w,'O', map)
    if p_w == 1:
        break

    n -= 1
    if n == 0:
        break

    cc = CT(map)

    map[cc - 1] = 'X'

    p_s = WL(p_w, 'X', map)
    if p_s == 1:
        break

    for i in range(5):
        print('')



for i in range(5):
    print('')
print(' ----------------')
print(' ㅣ ' + map[0] + ' ㅣ ' + map[1] + ' ㅣ ' + map[2] + ' ㅣ ')
print(' ----------------')
print(' ㅣ ' + map[3] + ' ㅣ ' + map[4] + ' ㅣ ' + map[5] + ' ㅣ ')
print(' ----------------')
print(' ㅣ ' + map[6] + ' ㅣ ' + map[7] + ' ㅣ ' + map[8] + ' ㅣ ')
print(' ----------------')
if p_w == 1:
    print('Player Win')
elif p_s == 1:
    print('Computer Win')
else:
    print('Draw')
