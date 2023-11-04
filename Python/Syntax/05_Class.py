import random


# a = {}
# a['hi'] = 'hihihi'
# a['bye'] = 'byebyebye'
# print(a['hi'])
# print(a['bye'])

# 클래스는 커멀 규칙(앞은 소문자 뒷자리는 대문자
# 함수는 _ 씀

# __init__ 초기값 클래스 쓸 때 가장 먼저 실행됨
# class의 (self)는 주소를 가르켜 어떤 값을 찾아갈 수 있음

class playerC():

    def __init__(self):
        self.hp = random.randrange(100, 150)
        self.mp = random.randrange(100, 150)
        self.speed = random.randrange(100, 150)
        self.item = 5

    def hit(self):
        if random.randrange(self.speed, 150) > 120:
            return self.hp * 0.1 // 1
        else:
            return 0

    def skill(self):
        return (self.hp * 0.1 + self.mp * 0.1) // 1

    def escape(self):
        if random.randrange(self.speed, 200) > 185:
            return 1

    def item_(self):
        if self.item > 0:
            return 1


def choice(q, a, b):
    if q == 1:
        if random.randrange(1, 3) == 1:
            b.hp -= a.skill()
            print('"a" skill')
        else:
            b.hp -= a.hit()
    elif q == 2:
        if a.item_() == 1:
            a.item -= 1
            a.hp += random.randrange(5, 10)
            a.mp += random.randrange(5, 10)
            a.speed += 5
    else:
        if a.escape() == 1:
            print('escaped')


c = {}
c['1'] = 'a > b hit'
c['2'] = '"a" item'
c['3'] = '"a" escape'
c[1] = 'b > a hit'
c[2] = '"b" item'
c[3] = '"b" escape'
a = playerC()
b = playerC()

# while a.hp > 0 and b.hp > 0:
#    print('a : hp({}), mp({}), speed({})'.format(a.hp, a.mp, a.speed))
#    print('b : hp({}), mp({}), speed({})'.format(b.hp, b.mp, b.speed))
#    q = input('1 : attack, 2 : item, 3 : escape ')
#    print('--------------------------')
#    print(c[q])
#    q = int(q)
#    if q == 1:
#        if random.randrange(1,3) == 1:
#            b.hp -= a.skill()
#            print('"a" skill')
#        else:
#            b.hp -= a.hit()
#    elif q == 2:
#        if a.item_() == 1:
#            a.item -= 1
#            a.hp += random.randrange(5,10)
#            a.mp += random.randrange(5,10)
#            a.speed += 5
#    else:
#        if a.escape() == 1:
#            print('"a" escaped')
#            break
#
#
#    q = random.randrange(1,4)
#    print(c[q])
#    if q != 3:
#        if random.randrange(1,3) == 1:
#            a.hp -= b.skill()
#            print('"b" skill')
#        else:
#            a.hp -= b.hit()
#    else:
#        if b.hp < a.hp:
#            if b.escape() == 1:
#                print('"b" escaped')
#                break
#        else:
#            if b.item_() == 1:
#                b.item -= 1
#                b.hp += random.randrange(5, 10)
#                b.mp += random.randrange(5, 10)
#                b.speed += 5

while a.hp > 0 and b.hp > 0:
    print('a : hp({}), mp({}), speed({})'.format(a.hp, a.mp, a.speed))
    print('b : hp({}), mp({}), speed({})'.format(b.hp, b.mp, b.speed))
    q = 0
    while q != '1' and q != '2' and q != '3':
        q = input('1 : attack, 2 : item, 3 : escape ')
    print('--------------------------')
    print(c[q])
    q = int(q)
    choice(q, a, b)
    q = random.randrange(1, 4)
    print(c[q])
    choice(q, b, a)

if a.hp > 0 and b.hp > 0 or a.hp < 0 and b.hp < 0:
    print('Tie')
elif b.hp < 0:
    print('"a" win')
else:
    print('"b" win')
