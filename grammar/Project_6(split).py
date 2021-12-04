#split = 자르기
#a = 123
#temp = a.split('2')
#a = [1,3]
#a, b = map(int, input().split(' '))
#
#for i in range(len(b)):
#   print(b[i], end=' ')


3 5


















#a = int(input())
#b = list(map(int, input().split(' ')))
#mi = b[0]
#ma = b[0]
#for i in range(1, a):
#    if b[i] < mi:
#        mi = b[i]
#    elif b[i] > ma:
#        ma = b[i]
#print(mi,ma)











#a = 8
#b = [1, 5, 8, 9, 10, 15, 23, 2]
#e = 0
#for i in range(a):
#    c = 0
#    if b[i] > 1:
#        for j in range(2, b[i]):
#            if b[i] % j == 0:
#                c = c + 1
#        if c == 0:
#            e = e + 1
#print(e)







#a = int(input())
#b = list(map(int, input().split(' ')))
#e = 0
#for i in range(a):
#    c = 0
#    for j in range(2, b[i] // 2 + 1):
#        if b[i] % j == 0 or b[i] < 2:
#            c = 1
#    if c == 0:
#        e = e + 1
#e = e - 1
#print(e)
