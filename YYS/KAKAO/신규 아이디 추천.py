def solution(new_id):
    # 알파벳 소문자: 97~122
    # 숫자: 48~57
    # 빼기: 45 점:46 밑줄: 95

    level1 = str.lower(new_id)
    level2 = ''
    for c in level1:
        n = ord(c)
        if 97 <= n <= 122 or n == 45 or n == 46 or n == 95 or 48 <= n <= 57:
            level2 += c
            # print(level2)

    while ".." in level2:
        level2 = level2.replace('..','.')

    level3 = level2
    #print(level3)

    level4 = level3.strip('.')
    #print(level4)

    if not level4:
        level4 = 'a'

    if len(level4) >= 16:
        level4 = level4[0:15]
        level4 = level4.strip('.')

    if len(level4) <= 2:
        last = level4[-1]
        while(not len(level4)==3):
            level4 += last
    return level4

print(solution("z-+.^."))