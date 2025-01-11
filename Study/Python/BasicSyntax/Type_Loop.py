print("Hello World")

a = 3
a = 4

# 4 int
print(a)
print(type(a))

# asdf str
a = "asdf"
print(a, type(a))

# 2.5 float
a = 2.5
print(a, type(a))

# + - * /
a = 4 + 5
print(a)
a = 4 - 5
print(a)
a = 4 * 5
print(a)
a = 4 / 5
print(a)
a = 4 % 5
print(a)

# ==, !=
a = 8
if a == 8:
    print("true")
a = 842
if a != 8:
    print("true")
    if a == 842:
        print("true")

num = int(input())
print(num)
print(type(num))

if num == 985:
    print("A")
elif 1 == num % 2:
    print("odd")
else:
    print("even")


print("hi")
print("hi")
print("hi")
print("hi")
print("hi")

for i in range(1):
    print("hi")

# for i(변수) in range(1[부터], 7[전까지])

for i in range(1, 10):
    print("*" * i)
for i in range(1, 10):
    print("*" * (10 - i))

num5 = input(int())
for i in range(1, num5):
    if type(num5 / i) == float:
        print("prime")
