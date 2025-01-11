n = int(input())
a = list(map(int, input().split(' ')))
b = 0
c = []
answer = 0

for i in range(n):
    if a[i] > 0:
        b += a[i]

    elif a[i] * -1 < b:
        b += a[i]

    else:
        c.append(b)
        b = 0

for i in range(len(c)):
    if c[i] > answer:
        answer = c[i]

print(answer, a, c)