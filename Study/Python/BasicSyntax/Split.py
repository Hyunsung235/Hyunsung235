# split = 자르기(나누기)
# a = 123
# a = a.split('2')
# a = [1,3]
# 2를 기준으로 잘라 변경됨(변수 > 리스트)
#
# a, b = map(int, input().split(' '))
# 2 3 을 각각 a b에 나눠 입력
#
# for i in range(len(b)):
#   print(b[i], end=' ')
# 123456을 1 2 3 4 5 6으로 나눠 출력
# 리스트, 변수 둘다 가능







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
