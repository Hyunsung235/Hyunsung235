# 분해
def decompose_korean(text):
    first = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
    second = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]
    third = [""] + ["ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ",
                   "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]

    def decompose_char(char):
        if '가' <= char <= '힣':
            code = ord(char) - 0xAC00
            cho = code // (21 * 28)
            jung = (code // 28) % 21
            jong = code % 28
            return [first[cho], second[jung], third[jong]] if third[jong] else [first[cho], second[jung]]
        else:
            return [char]

    g = []
    for c in text:
        x = decompose_char(c)
        if len(x) == 2:
            x.append(' ')
        if x[0] in first:
            g.append(x)
    return g

# 합채
def compose_korean(jamo_list):
    CHO = {v: i for i, v in
           enumerate(["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"])}
    JUNG = {v: i for i, v in enumerate(
        ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"])}
    JONG = {v: i for i, v in enumerate(
        [""] + ["ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ",
                "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"])}

    def compose_char(jamo):
        if len(jamo) == 3:
            cho, jung, jong = CHO[jamo[0]], JUNG[jamo[1]], JONG[jamo[2]]
        elif len(jamo) == 2:
            cho, jung, jong = CHO[jamo[0]], JUNG[jamo[1]], 0
        else:
            return jamo[0]
        code = 0xAC00 + cho * (21 * 28) + jung * 28 + jong
        return chr(code)
    return ''.join(compose_char(jamo) for jamo in jamo_list)
def change(one):
    listup = []
    for i in range(len(one)):

    # 탈락
        # 자음군 단순화
        if one[i][2] in ['ㄳ', 'ㄵ', 'ㄶ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㅀ', 'ㅄ', 'ㄺ', 'ㄻ', 'ㄿ']:
            if one[i][2] == 'ㄳ':
                one[i][2] = 'ㄱ'
            elif one[i][2] == 'ㄵ':
                one[i][2] = 'ㄴ'
            elif one[i][2] in ['ㄽ', 'ㄾ', 'ㅀ']:
                one[i][2] = 'ㄹ'
            elif one[i][2] == 'ㅄ':
                one[i][2] = 'ㅂ'
            elif one[i][2] == 'ㄻ':
                one[i][2] = 'ㅁ'
            elif one[i][2] == 'ㄿ':
                one[i][2] = 'ㅍ'
            elif one[i] == ['ㅂ', 'ㅏ', 'ㄼ'] or one[i] == ['ㄴ', 'ㅓ', 'ㄼ']:
                one[i][2] = 'ㅂ'
            elif one[i][2] == 'ㄺ':
                if i + 1 < len(one) and one[i + 1][0] == 'ㄱ':
                    one[i][2] = 'ㄹ'
                    one[i + 1][0] = 'ㄲ'
                else:
                    one[i][2] = 'ㄱ'
            listup.append('자음군 단순화')

        # ㅎ 탈락
        if i != len(one) - 1 and one[i][2] == 'ㅎ' and one[i + 1][0] == 'ㅇ':
            one[i][2] = ' '
            listup.append('ㅎ 탈락')

    # 축약
        # 거센소리 되기
        if i != len(one) - 1 and one[i][2] == 'ㅎ' and one[i + 1][0] in ['ㄱ', 'ㄷ', 'ㅂ', 'ㅈ']:
            harsh = {'ㄱ': 'ㅋ', 'ㄷ': 'ㅌ', 'ㅂ': 'ㅍ', 'ㅈ': 'ㅊ'}
            one[i][2] = ' '
            one[i + 1][0] = harsh[one[i + 1][0]]
            listup.append('거센소리 되기')
        if i != len(one) - 1 and one[i + 1][0] == 'ㅎ' and one[i][2] in ['ㄱ', 'ㄷ', 'ㅂ', 'ㅈ']:
            harsh = {'ㄱ': 'ㅋ', 'ㄷ': 'ㅌ', 'ㅂ': 'ㅍ', 'ㅈ': 'ㅊ'}
            one[i + 1][0] = harsh[one[i][2]]
            one[i][2] = ' '
            listup.append('거센소리 되기')
    # 교체
        # 구개음화(실질 형식 구별 불가)
        if i != len(one) - 1 and one[i][2] in ['ㄷ', 'ㅌ'] and one[i + 1][0] == 'ㅇ' and one[i + 1][1] in ['ㅣ',
                                                                                                                    'ㅑ',
                                                                                                                    'ㅕ',
                                                                                                                    'ㅛ',
                                                                                                                    'ㅠ']:
            if one[i][2] == 'ㄷ':
                one[i][2] = ' '
                one[i + 1][0] = 'ㅈ'
            if one[i][2] == 'ㅌ':
                one[i][2] = ' '
                one[i + 1][0] = 'ㅊ'
            listup.append('구개음화')

        # 음끝
        if one[i][2] not in ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅇ', ' ']:
            if one[i][2] in ['ㅋ', 'ㄲ']:
                one[i][2] = 'ㄱ'
            elif one[i][2] in ['ㅌ', 'ㅅ', 'ㅆ', 'ㅈ', 'ㅊ', 'ㅎ']:
                one[i][2] = 'ㄷ'
            elif one[i][2] == 'ㅍ':
                one[i][2] = 'ㅂ'
            listup.append('음끝')

        # 비음화
        if i != len(one) - 1 and one[i][2] in ['ㄱ', 'ㄷ', 'ㅂ'] and one[i + 1][0] in ['ㄴ', 'ㅁ', 'ㄹ']:
            if one[i][2] == 'ㄱ':
                one[i][2] = 'ㅇ'
            elif one[i][2] == 'ㄷ':
                one[i][2] = 'ㄴ'
            elif one[i][2] == 'ㅂ':
                one[i][2] = 'ㅁ'
            if one[i + 1][0] == 'ㄹ':
                one[i + 1][0] = 'ㄴ'
            listup.append('비음화')

        # 유음화
        if i != len(one) - 1 and one[i][2] == 'ㄹ' and one[i + 1][0] == 'ㄴ':
            one[i + 1][0] = 'ㄹ'
            listup.append('유음화')
        if i != len(one) - 1 and one[i][2] == 'ㄴ' and one[i + 1][0] == 'ㄹ':
            one[i][2] = 'ㄴ'
            listup.append('유음화')

        # 된소리되기
        if i != len(one) - 1 and one[i][2] in ['ㄱ', 'ㄷ', 'ㅂ'] and one[i + 1][0] in ['ㄱ', 'ㄷ', 'ㅂ', 'ㅅ', 'ㅈ']:
            dist = {'ㄱ': 'ㄲ', 'ㄷ': 'ㄸ', 'ㅂ': 'ㅃ', 'ㅅ': 'ㅆ', 'ㅈ': 'ㅉ'}
            one[i + 1][0] = dist[one[i + 1][0]]
            listup.append('된소리되기')

    # 연음
        if i != 0 and one[i][0] == 'ㅇ' and one[i - 1][2] != ' ':
            one[i][0] = one[i - 1][2]
            one[i - 1][2] = ' '

    for j in one:
        if j[2] == ' ':
            j.pop(2)
    return one, listup

while True:
    dain = input("글자를 입력하세요(end를 입력하면 종료합니다.): ")
    if dain == 'end':
        print('프로그램을 종료합니다.')
        break
    korean = decompose_korean(dain)
    a, b = change(korean)
    if not b:
      b = '변경사항 없음'
    print(f'발음: [{compose_korean(a)}], 과정: {b}')