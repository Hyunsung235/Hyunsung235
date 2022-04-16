import random

# z = random.randrange(1,1000)
#
# a = 1000 - z
# b = [500,100,50,10,5,1]
# c = 0
# print(a)
# for i in range(len(b)):
#    while a > b[i] or a == b[i]:
#        a -= b[i]
#        c +=1
# print(c)
# 5585
#
# ================================================================================
#
#
A = list(map(int, input()))
b = 0
c = ''
A.sort(reverse=True)

for i in range(len(A)):
    b += A[i]
    c = c + str(A[i])

if b % 3 == 0 and A[len(A) - 1] == 0:
    print(int(c))
else:
    print(-1)
