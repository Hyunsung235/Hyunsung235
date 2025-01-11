s = input()

check = {chr(a): -1 for a in range(ord('a'), ord('z') + 1)}

for i, c in enumerate(s):
    if check[c] == -1:
        check[c] = i

print(*check.values())
# * 의미 : 공백으로 나누어 출력
