from collections import deque

a = []
b = deque()
c = 1
e = 1
b.append([0, 0])

for i in range(3):
    a.append(list(map(int, input().split(' '))))

while True:
    c, d = b.popleft()
    a[c][d] = e

    if len(a[c]) == d + 1:
        b.append([c + 1, 0])

    else:
        b.append([c, d + 1])
    print(a,c,d)
    e += 1
    if len(a) == c:
        break
print(len(a),c)
print(a)
