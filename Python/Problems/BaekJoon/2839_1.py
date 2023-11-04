suger = int(input())
three = 0
five = 0

while suger - 3 >= 0 and suger % 5 != 0:
    suger -= 3
    three += 1
    if three == 5:
        five += 3
        three -= 5

while suger - 5 >= 0 and suger % 5 == 0:
    suger -= 5
    five += 1

if suger == 0:
    print(three + five)

else:
    print(-1)