#id_list = []
#pwd_list = []
#
#while len(pwd_list) < 5:
#    c = 0
#    id_input = input('id : ')
#    for i in range(len(pwd_list)):
#        if id_list[i] == id_input:
#            c = 1
#    if c != 0:
#        print('이미 있는 id 입니다 다시 입력해주세요')
#    else:
#        pwd_input = (input('pwd : '))
#        id_list.append(id_input)
#        pwd_list.append(pwd_input)
#        print('id :', len(id_list), ' pwd : ', len(pwd_list))
#
#print('id : ', id_list)
#print('pwd : ', pwd_list)
#원본
#
#
#
#
#
#p = str(input('pwd = '))
#l = '!@#$%'
#for i in range(len(p)):
#    for ii in range(5):
#        if p[i] == l[ii]:
#            print('true')
#
#
#
#
#
#
#
#
#
#id_list = []
#pwd_list = []
#a = '!@#$%'
#
#while len(pwd_list) < 5:
#    c = 0
#    count_2 = 0
#    id_input = input('id를 입력하세요(3글자 이상) : ')
#    if len(id_input) >= 3:
#        for i in range(len(pwd_list)):
#            if id_list[i] == id_input:
#                c = 1
#        if c != 0:
#            print('이미 있는 id 입니다 다시 입력해주세요')
#        else:
#            while count_2 != 1:
#                pwd_input = (input('pwd : '))
#                for n in range(len(p)):
#                    for n_2 in range(5):
#                        if p[n] == l[n_2]:
#                            count_2 = 1
#                if count_2 == 1:
#                    id_list.append(id_input)
#                    pwd_list.append(pwd_input)
#                    print('id :', len(id_list), ' pwd : ', len(pwd_list))
#                else:
#                    print('특수문자를 추가해 주세요')
#   else:
#        print('너무 짧은 id 입니다 다시 입력해주세요')
#
#print('id : ', id_list)
#print('pwd : ', pwd_list)
#
