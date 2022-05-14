a = []
b = ''
c = ''
e = 0
n = 3


def init():
    a = []
    return a


def push(a,b):
    if len(a) == 3:
        print('overflow')
        c = 'break'
        return c

    else:
        c = b.split(')')
        a.append(int(c[0]))
        return a


def pop(a):
    if len(a) == 0:
        print('underflow')
        b = 'break'
        return b

    else:
        print(a[len(a) - 1])
        del a[len(a) - 1]
    return a


def enqueue(a,b):
    if len(a) == 3:
        print('overflow')
        c = 'break'
        return c

    else:
        c = b.split(')')
        a.append(int(c[0]))
        return a


def dequeue(a):
    if len(a) == 0:
        print('underflow')
        b = 'break'
        return b

    else:
        print(a[0])
        del a[0]
    return a


while True:
    print(a)
    c, b = input().split('(')
    if c == 'init':
        e = init()

    elif c == 'push':
        e = push(a, b)

    elif c == 'pop':
        e = pop(a)

    elif c == 'enqueue':
        e = enqueue(a,b)

    else:
        e = dequeue(a)

    if e == 'break':
        break

    else:
        a = e