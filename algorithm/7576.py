from collections import deque

m, n = map(int, input().split(' '))
farm = []
visited = [[0 for _ in range(m)] for _ in range(n)]
arrows = [[1, 0], [0, -1], [-1, 0], [0, 1]]

for i in range(n):
    farm.append(list(map(int, input().split())))

k = deque()
for i in range(len(farm)):
    for j in range(len(farm[i])):
        if farm[i][j] == 1:
            k.append([i, j])

while len(k) > 0:
    x, y = k.popleft()
    for arrow in arrows:
        a = x + arrow[0]
        b = y + arrow[1]
        if a < 0 or a >= n or b < 0 or b >= m:
            continue
        if farm[a][b] == 0:
            k.append([a, b])
            farm[a][b] = 1
            visited[a][b] = visited[x][y] + 1

values = []
flag = 1
for i in range(len(farm)):
    for j in range(len(farm[i])):
        if farm[i][j] == 0:
            flag = 0
            break
        else:
            values.append(visited[i][j])

if flag == 0:
    print(-1)
else:
    print(max(values))