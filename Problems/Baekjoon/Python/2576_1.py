a = []
for i in range(7):
    b = int(input())
    if b % 2 == 1:
        a.append(b)


if len(a) > 0:
    m = a[0]
    h = 0

    for i in a:
        if m > i:
            m = i
        h += i

    print(h)
    print(m)

else:
    print(-1)