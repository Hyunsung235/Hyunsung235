a = 3
b = 2

if a == 3 and b == 2:
    print('y')
if a == 3 or b == 1:
    print('y')

#a = int(input("Enter the number : "))
count = 0

# 9 // 2 = 4
for i in range(2, a // 2):
    if a % i == 0:
        count += 1


if count == 0:
    print('prime')
else:
    print('not prime')



for o in range(13):
    if o == 10:
        continue
    print(o)

#a = int(input("Enter the number : "))
for i in range(2, a//2+1):
    if a % i == 0:
        print('prime')
        break







import random

b = []
c = []
for i in range(1, 101):
    b.append(i)
print(b)

for i in range(101):
    n = random.randrange(1, 101)
    c.append(n)
print(c)

