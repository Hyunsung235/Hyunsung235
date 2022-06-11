a = [0, 1]
for i in range(int(input())):
    a.append(a[i] + a[i + 1])
print(a[len(a) - 2])
