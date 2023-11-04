h = 0
m = 0
for i in range(7):
    b = int(input())
    if b % 2 == 1:
        h += b
        if m == 0 or m > b:
            m = b

if m > 0:
    print(h)
    print(m)

else:
    print(-1)