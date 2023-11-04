# 가장 가까운 직사각형의 경계선 찾기
#틀림
a = input()
a = a.split(' ')
for i in range(4):
    a[i] = int(a[i])
b = [a[2] - a[0], a[3] - a[1]]
print(a)
print(b)
if b[0] <= b[1]:
    print(b[0])
else:
    print(b[1])
