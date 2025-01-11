N = int(input())  #테스트 데이터
result = "" #빈 문자열 생성

for i in range(N):
    testcase = input()
    cnt = 0
    for c in testcase:
        if c == '(':
            cnt += 1
        else: # ')'
            cnt -= 1
        if cnt < 0:  #괄호가 완성되지 않는 첫번째 경우 () (())  (()))(
            result += "NO\n"
            break
    else:
        if cnt == 0:  #() (())
            result += "YES\n"
        else:
            result += "NO\n"

print(result)
