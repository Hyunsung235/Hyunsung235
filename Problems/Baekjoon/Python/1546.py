subject = int(input())
number = input().split(' ')
max = int(number[0])
total = 0
for i in range(subject):
    if max < int(number[i]):
        max = int(number[i])
for i in range(subject):
    total += int(number[i]) / max * 100
print(total / subject)
