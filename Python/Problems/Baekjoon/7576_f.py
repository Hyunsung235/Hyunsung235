from collections import deque


m, n = map(int, input().split(' '))

a = []
for i in range(n):
    a.append(list(map(int, input().split(' '))))

b = [[1, 0], [-1, 0], [0, 1], [0, -1]]

r = deque()

c = 0

o = 0

e = []

f = 0

for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            r.append([i, j])

if len(r) == 0:
    o = -1


while o == 0:
    for i in range(len(r)):
        y, x = r.popleft()

        for p in range(len(e)):
            if e[p][0] == y and e[p][1] == x:
                f = 1

        if f == 0:
            a[y][x] = 1
            for j in range(4):
                y_i, x_i = y + b[j][0], x + b[j][1]
                if -1 < y_i < n and -1 < x_i < m and a[y_i][x_i] == 0:
                        r.append([y_i, x_i])
                        a[y_i, x_i] = 1

    e.append([y, x])
    print(r)

    if len(r) == 0:
        break

    c += 1

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            o = 1
            break

if o == 1:
    print(-1)

elif o == -1:
    print(0)

else:
    print(c)