n = int(input())
l = list(map(int, input().split(' ')))
a = []
b = 0
c = 0

for i in range(n):
    if l[i] > 0:
        b += l[i]

        if i == n - 1:
            a.append(b)

    else:
        if b > 0:
            a.append(b)
        a.append(l[i])
        b = 0

print(a)
# [ 2 5 -9 7 3 -2 5 ] > [ 7 -9 10 -2 5]


b = a[0]
m = a[0]

for i in range(1, len(a)):
    if a[i] > 0:
        b += a[i]

    else:
        if i < len(a) - 1:
            if a[i + 1] < 0:
                c += a[i]

            elif b + c + a[i] > 0:
                b += c + a[i]

            elif m < b:
                m = b
                b = 0

            else:
                b = 0

        elif m < a[i]:
            m = a[i]
    print(i, a[i], b, m, c)

print(b)