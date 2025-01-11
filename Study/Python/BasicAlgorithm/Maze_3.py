from collections import deque

m = []
arrows = [[-1, 0], [1, 0], [0, 1], [0, -1]]
l = deque
n = []
map_h = int(input())


for i in range(map_h):
    m.append(list(map(int, input().split(' '))))

    for j in range(len(m[i])):
        if m[i][j] == 1:
            l.append([i, j])




while True:
    x, y, n = l.popleft()

    if map[x][y] == 2:
        break

    for a in arrows:
        x_i, y_i = x + a[0], y + a[1]

        if 0 <= x_i < map_h and 0 <= y_i < len(map[map_h]):
            if m[x_i][y_i] == 0:
                m[x_i][y_i] = 1
                l.append([x_i, y_i, n.append(x_i, y_i)])

print(n)
