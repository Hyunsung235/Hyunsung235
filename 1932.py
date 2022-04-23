# 1932
a = []
for i in range(int(input())):
    a.append(list(map(int, input().split(' '))))
for i in range(len(a) - 1):
    for j in range(len(a[len(a) - 2 - i])):
        if a[len(a) - 1 - i][j] < a[len(a) - 1 - i][j + 1]:
            a[len(a) - 2 - i][j] += a[len(a) - 1 - i][j + 1]
        else:
            a[len(a) - 2 - i][j] += a[len(a) - 1 - i][j]
print(a[0][0])