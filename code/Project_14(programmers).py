#프로그래머스_나머지가 1이 되는 수 찾기
def solution(n):
    for i in range(1,1000000):
        if n % i == 1:
            answer = i
            return answer

#프로그래머스_로또의 초고 순위와 최저 순위
def solution_2(lottos, win_nums):
    a = 7
    b = 0
    c = 0
    for i in range(6):
        for j in range(6):
            if lottos[i] == win_nums[j]:
                a -= 1
    for i in range(6):
        if lottos[i] == 0:
            b += 1
    c = a - b
    if a == 7:
        a -= 1
    if c == 7:
        c -= 1
    answer = [c, a]
    return answer

#프로그래머스_부족한 금액 계산하기
def solution_3(price, money, count):
    b = 0
    for i in range(1, count + 1):
        b += price * i
    if money < b:
        answer = b - money
    else:
        answer = 0
    return answer

#프로그래머스_부족한 금액 계산하기
def solution_4(people, limit):
    people.sort()
    a = []
    b = 0
    c = []
    for i in range(len(people)):
        c.append('X')
    d = 0
    e = 0
    l = limit

    while d != len(people):
        while c[d] != 'X':
            d += 1
        e += 1

        c[d] = 'O'
        l = limit
        l -= people[d]
        a = []

        b = 1
        while people[len(people) - b] < l:
            b += 1
        c[b] = 'O'

    answer = e
    return answer
