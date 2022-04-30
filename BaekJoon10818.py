#가장 큰 수, 가장 작은 수 찾기

a = int(input())
b = input()
b = b.split(' ')
for i in range(len(b)):
    b[i] = int(b[i])
minmax = [b[0], b[0]]
for i in range(a):
    if b[i] < minmax[0]:
        minmax[0] = b[i]
    if b[i] > minmax[1]:
        minmax[1] = b[i]
for i in range(2):
    print(minmax[i], end=' ')
