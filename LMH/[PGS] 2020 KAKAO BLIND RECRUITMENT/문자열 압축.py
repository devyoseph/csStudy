"""
PGS
문자열 압축
level2
40분
https://school.programmers.co.kr/learn/courses/30/lessons/60057
"""
def check(s, num):
    cnt = 1
    char = s[:num]
    res = ''
    for i in range(num,len(s)+num,num): # len(s)+num 까지 범위로 잡아야 마지막으로 일치하지 않는 부분 추가하는 코드 수행할 수 있다.
        print(i)
        if s[i:i+num] == char:
            cnt += 1
        else:
            if cnt > 1: # 슬라이싱한 문자열의 개수가 1일때는 cnt 생략한다.
                res += str(cnt)
            res += char
            # 값 초기화
            cnt = 1
            char = s[i:i+num]
    print('res', f'{res} {len(res)}')
    return len(res)

def solution(s):
    answer = len(s)
    for num in range(1,len(s)//2+1): # 1~len(s)//2까지 문자열 검사
        answer = min(answer, check(s,num))
    return answer


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
