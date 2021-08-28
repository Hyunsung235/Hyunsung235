#i = 1
#while i < 14:
#    print('*' * i)
#    i = i + 1


#s = 0
#i = 0
#while i < 100:
#    s = 0
#    i = i + 1
#    if i // 10 % 3 == 0 and i // 10 != 0:
#        s = s + 1
#    if i % 10 % 3 == 0 and i % 10 != 0:
#        s = s + 1
#    if s == 0:
#        print(i)
#    else:
#        print('*' * s)



for i in range(1, 100):

    one = i % 10
    ten = i // 10
    first_if = one % 3 == 0 and one != 0
    second_if = ten % 3 == 0 and ten != 0

    if first_if and second_if:
        print('**')
    elif first_if or second_if:
        print('*')
    else:
        print(i)