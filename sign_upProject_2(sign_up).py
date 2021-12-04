# id = []
# pwd = []
#
# id_input = str(input('id : '))
# pwd_input = str(input('id : '))
#
# if id_input > 7:
#    count = 0
#    for i in range():
#        if id[i] == id[len]:
#            count = 1
#    if count == 0:
#        count = 0
#        for i in range(pwd[len(pwd)]):
#            if pwd[len(pwd)][i] == '!' or '@' or '#' or '$' or '5':
#                print('회원가입 되었습니다')
#                count = 2
#            else:
#               print('비밀번호에 특수문자(!@#$%)중 하나를 추가해주세요')
#    else:
#        print('이미 있는 아이디입니다')
# else:
#    print('아이디를 8자 이상으로 입력해주세요')
# if count != 2:
#    id13
#
#
#
#for n in range(1,10):
#    for i in range(1,10):
#        print('{} X {} = {}'.format(n,i,n * i))
#
#asdf = '!@#$%'
#id_list = []
#pwd_list = []
#
#
#
#for i in range(5):
#    qwerty = 0
#    while qwerty == 0:
#        id_input = str(input('id : '))
#        pwd_input = str(input('pwd : '))
#        if len(id_input) > 7:
#            count = 0
#            for i in range(len(id_list)):
#                if id_list[i] == id_input:
#                    count = 1
#            if count == 0:
#                for n in range(len(pwd_input)):
#                    for nn in range(len(asdf)):
#                        if pwd_input[n] == asdf[nn]:
#                            count = 1
#                if count == 1:
#                    id_list.append(id_input)
#                    pwd_list.append(pwd_list)
#                    print('회원가입에 성공하였습니다')
#                else:
#                    print('특수문자(!@#$%) 중 하나를 추가해주세요')
#            else:
#                print('이미 있는 아이디 입니다')
#        else:
#            print('id 를 8자 이상으로 입력해주세요')
#n = []
#c = [0,0,0,0,0]
#import random
#for i in range(100):
#    a = int(random.randrange(1,6))
#    n.append(a)
#    c[n[i] - 1] += 1
#print(c)

asdf = '!@#$%'
id_list = []
pwd_list = []

for i in range(5):
    qwerty = 0
    while qwerty == 0:
        id_input = str(input('id : '))
        pwd_input = str(input('pwd : '))
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
                    id_list.append(id_input)
                    pwd_list.append(pwd_list)
                    print('회원가입에 성공하였습니다')
                else:
                    print('특수문자(!@#$%) 중 하나를 추가해주세요')
            else:
                print('이미 있는 아이디 입니다')
        else:
            print('id 를 8자 이상으로 입력해주세요')


for a in range(5)
