# 9095
b = [1,2,4]
for i in range(int(input())):
    a = int(input())
    if len(b) < a:
        for j in range(len(b) + 1, a + 1):
            b.append(b[j-2] + b[j-3] + b[j-4])
        print(b[a - 1])
    else:
        print(b[a - 1])