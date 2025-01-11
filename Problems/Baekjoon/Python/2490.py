y = ['E', 'A', 'B', 'C', 'D']
for i in range(3):
    a = list(map(int, input().split(' ')))
    s = 4
    for i in a:
        s -= i
    print(y[s])