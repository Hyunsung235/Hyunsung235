a = int(input())
if a == 1:
    b = int(input())
    print(b * b)
else:
    b = input().split(' ')
    c = [int(b[0]), int(b[0])]
    for i in range(len(b)):
        if c[0] < int(b[i]):
            c[0] = int(b[i])
        if c[1] > int(b[i]):
            c[1] = int(b[i])
    print(c[0] * c[1])
