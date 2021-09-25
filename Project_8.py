import random


# function / 함수
# def cal_sum(x, y):
# z = x + y
# return z
# 설명서


# print(cal_sum(3, 2)
#
# result = cal_sum(3, 2)
# print(result)
# 사용


# 함수에다가 필요한 코드를 짜두고
# 필요할 때 마다 가져와서 쓴다
# 사용법


# return (함수 종료 / 값을 반환)
# return 이 없으면 값이 없음


#a = []
#b = 0
#
#
#def random_(x):
#    for i in range(10):
#        b = random.randrange(1,101)
#        a.append(b)
#    return x
#
#def select(x, y, l):
#    x = l[0]
#    y = l[0]
#    for i in range(10):
#        if x < l[i]:
#            x = l[i]
#        if y > l[i]:
#            y = l[i]
#    return 'max : 'x, y, l
#
#def use(x):
#    random_(x)
#    select(max,min,x)
#
#
#print(use(a))

#a = []
#max = 0
#min = 0
#
#def make_random_list():
#    a = []
#    for i in range(10):
#        random_num = random.randrange(1,100)
#        a.append(random_num)
#    return a
#
#def find_max_value(a):
#    max_value = a[0]
#    for i in range(len(a)):
#        if max_value < a[i]:
#            max_value = a[i]
#    return max_value
#
#temp_list = make_random_list()
#result = find_max_value(temp_list)
#print(result, temp_list)\


def win_or_lose(user,computer,user_coin):
    if user == computer:
        print('Tie')
    elif user == 'r' and computer == 's' or user == 's' and computer == 'p' or user == 'p' and computer == 'r':
        print('User Win')
        user_coin += 200
    else:
        print('Computer Win')
        user_coin -= 200
    return user_coin

rsp = ['r','s','p']
user_coin = 600
computer_coin = 600
while user_coin > 0 and computer_coin > 0:
    user = input('User(r/s/p) : ')
    computer = rsp[random.randrange(3)]
    print('computer(r/s/p) : ',computer)
    user_coin = win_or_lose(user,computer,user_coin)
    computer_coin = 1200 - user_coin
    print('User coin : ',user_coin,' / Computer coin : ',computer_coin)









id_list = []
pwd_list = []
def sign_up(id_input,pwd_input):
    asdf = '!@#$%'
    a = 0
    if len(id_input) > 7:
        count = 0
        for i in range(len(id_list)):
            if id_list[i] == id_input:
                count = 1
        if count == 0:
            for n in range(len(pwd_input)):
                for nn in range(len(asdf)):
                    if pwd_input[n] == asdf[nn]:
                        count = 1
            if count == 1:
                a = 1
                print('회원가입에 성공하였습니다')
            else:
                print('특수문자(!@#$%) 중 하나를 추가해주세요')
        else:
            print('이미 있는 아이디 입니다')
    else:
        print('id 를 8자 이상으로 입력해주세요')
    return a




for i in range(5):
    id_input = str(input('id : '))
    pwd_input = str(input('pwd : '))
    b = sign_up(id_input, pwd_input)
    if b == 1:
        id_list.append(id_input)
        pwd_list.append(pwd_input)