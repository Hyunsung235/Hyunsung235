a = int(input())
b = int(input())
c = int(input())
d = a * b * c
d = str(d)
e = [0,0,0,0,0,0,0,0,0,0]
for i in range(len(d)):
    e[int(d[i])] += 1
for i in range(len(e)):
    print(e[i])