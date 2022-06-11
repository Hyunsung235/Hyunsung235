from collections import deque
deq = deque()
deq.append([0, 0])


arr = []
for i in range(int(input())):
    arr.append(list(map(int, input().split(' '))))
print(arr)

#a = 0
#while True:
#    a += 1
#    x, y = deq.popleft()
#    arr[x][y] = a
#    print(arr)
#
#    if x == len(arr) - 1 and y == len(arr[len(arr) - 1]) - 1:
#        break
#
#    elif y == len(arr[len(arr) - 1]) - 1:
#        deq.append([x + 1, 0])
#    else:
#        deq.append([x, y + 1])

arrows = [[0, 1], [0, -1], [1, 0], [0, 1]]
n = []
b = 0
c = 0
d = 0
e = 0
while True:
    x,y = deq.popleft()
    for i in range (len(arrows)):
        if arr[x += arrows[i][0]][y += arrows[i][1]] == 1:
