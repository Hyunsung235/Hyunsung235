for i in range(int(input())):
    a = input()
    b = 0
    c = 0
    for j in range(len(a)):
        if a[j] == '(':
            b += 1
        else:
            c += 1
    if b == c:
        for k in range(len(a) // 2 - 1, len(a)):
            if a[k] == '(':
                b += 1
            else:
                c += 1
        if c == b:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
