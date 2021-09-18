#리스트에 랜덤하게 100개 넣고 그 다음에 가장 큰/작은거 뽑기
#문자열을 input으로 받아서 거꾸로 출력하기
#효율적으로 랜덤한 숫자(1~100)중 하나를 찾기

import random

#n = []
#a = 0
#
#for i in range(10):
#    a = random.randrange(1,101)
#    n.append(a)
#
#c = n[0]
#b = n[0]
#for i in range(len(n)):
#    if b < n[i]:
#        b = n[i]
#    if c > n[i]:
#        c = n[i]
#print(b,' ',c,' ',n)
#
#
#
#d = input('input : ')
#e = str()
#for i in range(len(d)):
#    e = e + d[len(d) - (i + 1)]
#print('output : ',e)

f = random.randrange(1,101)
print(f)

g = 100
h = 0
j = 0

for i in range(5):
    if g // 2 < f:
        j = i
        break
    elif g // i + 2 < f:
        h = g // i + 2
    else:







# 71
# 50
# 50 75
# 12.5
# 62.5 75
#





