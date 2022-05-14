a, b = 100, 100
for i in range(int(input())):
    c, d = map(int, input().split(' '))
    if c > d:
        b -= c
    elif c < d:
        a -= d

print(a)
print(b)