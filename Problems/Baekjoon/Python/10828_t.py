a = ''
b = []
c = 0
for i in range(int(input())):
    a = input().split(' ')

    if a[0] == 'push':
        b.append(a[1])

    elif a[0] == 'pop':
        if len(b) == 0:
            print(-1)
        else:
            print(b[-1])
            b.pop(-1)

    elif a[0] == 'size':
        print(len(b))

    elif a[0] == 'empty':
        if len(b) == 0:
            print(1)
        else:
            print(0)

    else:
        if len(b) == 0:
            print(-1)
        else:
            print(b[-1])
