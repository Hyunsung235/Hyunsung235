import random

n = []
min_n = 0
max_n = 0

for i in range(10):
    n.append(random.randrange(1, 20))


min_n, max_n = n[0], n[0]
for i in range(len(n)):
    if min_n > n[i]:
        min_n = n[i]

    if max_n < n[i]:
        max_n = n[i]

print('n : {} , min : {} , max : {}'.format(n, min_n, max_n))



for i in range(len(n)):
    for j in range(len(n) - 1):
        if n[j] > n[j + 1]:
            n[j], n[j + 1] = n[j + 1], n[j]
            print(n)
print(n)