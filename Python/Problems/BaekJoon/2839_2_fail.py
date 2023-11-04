suger = int(input())

five = suger // 5
suger = suger % 5

three = suger // 3
suger = suger % 3

if suger == 1 and five >= 1:
    five -= 1
    three += 2
    suger -= 1

elif suger == 2 and three >= 1:
    five += 1
    three -= 1
    suger -= 2

if suger == 0:
    print(five + three)

else:
    print(-1)