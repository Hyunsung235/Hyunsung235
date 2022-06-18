from collections import deque

maze = []
deq = deque()

a = [[0, 1], [0, -1], [1, 0], [-1, 0]]
deq.append([0, 0])

for i in range(3):
    maze.append(list(map(int, input().split(' '))))

while True:
        x, y = deq.popleft()
        maze[y][x] = 2
        for i in range(4):
            if maze[y + a[i][1]][x + a[i][0]] == 1:
                p, q = maze[y + a[i][1]], maze[x + a[i][0]]
                if p != -1 and p != len(maze[0]) and q != -1 and q != len(maze[0]):
                    deq.append([p, q])

        print(maze)




#    e = 0
#    for i in range(4):
#        y, x = deq[len(deq) - 1]
#        d.append([y, x])
#        maze[y][x] == '2'
#        if x != len(maze[y]) - 1 and y != len(maze) - 1:
#            if maze[y + a[i][1]][x + a[i][0]] == '1':
#                for j in range(len(d)):
#                    if maze[y + a[i][1]][x + a[i][0]] == d[j]:
#                        e = 1
#                if e == 0:
#                    deq.append([y + a[i][1], [x + a[i][0]]])
#
#    y, x = deq.popleft()
#    if x == len(maze[y]) - 1 and y == len(maze) - 1:
#        break
#
#    print(maze)