import random

#bridge = []
#for i in range(17):
#    random_12 = random.randrange(1,3)
#    bridge.append(random_12)
#
#r = 0
#h = 8
#while h > 0 or r < 16:
#    a = int(input('1 = Right / 2 = Left : '))
#    if a == bridge[r]:
#        print('success')
#        r = r + 1
#    else:
#        print('fail')
#        h = h - 1
#if r < 16:
#    print('SUCCESS!')
#else:
#    print('FAIL!')

r1 = ['7','8','9']
r2 = ['4','5','6']
r3 = ['1','2','3']
nc_i = 0
nc = []
n = [1,2,3,4,5,6,7,8,9]
r = 1
wl = 0
while r < 9 and wl < 1:
    for i in range(5):
        print(' ')
    print(r1)
    print(r2)
    print(r3)
    print('User = O / Computer = X')
    c = int(input('Your turn (1~9) : '))
    if n[c - 1] == c:
        n[c - 1] = 'X'
        if c > 6:
            r1[c - 7] = 'O'
        elif c > 3 and c < 7:
            r2[c - 4] = 'O'
        else:
            r3[c - 1] = 'O'
    nc = []
    for i in range(9):
        if n[i] != 'X':
            nc.append(n[i])
    nc_i = nc[random.randrange(len(nc))]
    n[nc_i - 1] = 'X'
    if nc_i > 6:
        r1[nc_i - 7] = 'X'
    elif nc_i > 3 and nc_i< 7:
        r2[nc_i - 4] = 'X'
    else:
        r3[nc_i - 1] = 'X'

#승패 없음
