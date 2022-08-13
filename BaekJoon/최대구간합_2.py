n = int(input())
l = list(map(int, input().split(' ')))
add = 0
b = []

if max(l) > 0:
    for i in range(n):
        add += l[i]

        if l[i] < 0:
            b.append(add - l[i])

        if add < 0:
            add = 0
    b.append(add)
    print(max(b))
else:
    print(max(l))