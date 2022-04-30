a = [0,1]
for i in range(int(input()) - 1):
    a.append(a[len(a) - 1] + a[len(a) - 2])
print(a[len(a) - 1])
