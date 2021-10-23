import random

c = input()

#클래스 = 붕어빵 틀
#규칙 class [이름]():
#규칙 2 이름 두번째 단어 첫글짜는 대문자 classPrint
# __init__() == 초기화 제일 먼저 초기 설정 해두는것
# '{}' 빈공간 '{}'.format(b.hp) 이런식으로 채워 넣을수 있음

# self.hp
# self,np
#class makeA():
#    def print_Test(self):
#        print("hi")
#
#    def print_Test2(self):
#        print('bye')
#
#a = makeA()
#a.print_Test2()

class makeCh():

    def __init__(self):
        self.hp = random.randrange(1,10000)
        self.mp = random.randrange(1,10)
        self.skillP = 10011 - self.hp - self.mp

    def hit(self):
        return self.mp * 0.1

    def skill(self):
        return self.mp * self.skillP


a = makeCh()
print("a character hp : {} , mp : {} , Skill : {}".format(a.hp, a.mp, a.skillP))

b = makeCh()
print("b character hp : {} , mp : {} , SKill : {}".format(b.hp, b.mp, b.skillP))

print(' ')

while b.hp > 0 and a.hp > 0:

    if random.randrange(1,5) == 1:
        b.hp =- a.skill()
        print('a skill')
    else:
        b.hp =- a.hit()
    #print("after b character hp : {} , mp : {}".format(b.hp, b.mp))

    if random.randrange(1,5) == 1:
        a.hp = a.hp - b.skill()
        print('b skill')
    else:
        a.hp = a.hp - b.hit()
    #print("after a character hp : {} , mp : {}".format(a.hp, a.mp))


if b.hp > 0:
    print('b win')
else:
    print('a win')

#1:33