import random


# Bubble Sorting(버블 정렬)
# 1번과 2번을 비교하여 정렬, 2번과 3번, 3번과 4번 등등
# 1, 8, 5, 4, 9
# 1, 8, 5, 4, 9
# 1, 5, 8, 4, 9
# 1, 5, 4, 8, 9
# 1, 5, 4, 8, 9
# 1, 5, 4, 8, 9
# 1, 4, 5, 8, 9
# 1, 4, 5, 8, 9
# 1, 4, 5, 8, 9

d = 0

# selective sort(선택 정렬)
# 가장 낮은 숫자를 가장 앞으로 위치를 변경하면서 정렬
# 5, 7, 2, 6, 5
# 2, 7, 5, 6, 5
# 2, 5, 7, 6, 5
# 2, 5, 5, 6, 7
# 2, 5, 5, 6, 7

e = 0

# 리스트 안, 변수에서 위치 변경
# c = b, b = a, a = c
# ==
# a, b = b, a

f = 0

# 좋은 코드 - 간결하고, 확실하고, 효율성이 좋고 또 용량이 적은 코드
# ㅁㄴㅇㄻㄴㅇㄻㄴㅇ


def bubble_sort(number, CDEF):
    a_list = []
    # b_index = 0
    for i in range(number):
        a_list.append(random.randrange(1, 101))
    print('-----', a_list, '-----')
    for j in range(len(a_list)):
        for i in range(len(a_list) - 1):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                # b_index = a_list[i + 1]
                # a_list[i + 1] = a_list[i]
                # a_list[i] = b_index
                if CDEF == 1:
                    print(a_list)
    print('-----', a_list, '-----')
    return


def selective_sort(number, CDEFG):
    a_list = []
    for i in range(number):
        a_list.append(random.randrange(1, 101))
    print('-----', a_list, '-----')
    min_index = len(a_list) - 1
    for j in range(len(a_list)):
        for i in range(j, len(a_list)):
            if a_list[i] < a_list[min_index]:
                min_index = i
        a_list[j], a_list[min_index] = a_list[min_index], a_list[j]
        min_index = len(a_list) - 1
        if CDEFG == 1:
            print(a_list)
    print('-----', a_list, '-----')
    return


while True:
    A = input('a or b : ')
    B = int(input('2 ~ : '))
    CDE = int(input('1 or 2 : '))
    if A == 'a':
        bubble_sort(B, CDE)
    if A == 'ab':
        bubble_sort(B, CDE)
        selective_sort(B, CDE)
    else:
        selective_sort(B, CDE)
