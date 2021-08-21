import random

# a = int(input("number : "))
# if a % 2 == 1:
# print('odd')
# else:
# print('even')


# for i in range(1, 11):
# print('*' * i)


# a: int = int(input('number : '))
# b = 0
# for i in range(2, a):
# if a % i == 0:
# b = 1
# if b == 1:
# print('not prime')
# else:
# print('prime')


# a = 0
# b = []
# for i in range(10):
#   a = random.randrange(101)
#  b.append(a)
# print(b)
+-
# for i in range(10):
#   if b[i] >= c:
# if b[i] <= d:
#     d = b[i]
# print('최대값 : ', c)
# print('최소값 : ', d)


# e = random.randrange(15)
# f = []
# for i in range(1, e // 2 + 2):
# if e % i == 0:
#   f.append(i)
# print('숫자 : ', e)
# print('약수 : ', f)


#효율적이게 랜덤한 숫자 찾기
a = random.randrange(100)
b = 100
for i in range(4):
b = b - 5