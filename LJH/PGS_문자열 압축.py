'''
PGS
문자열 압축
lv 2
30분
https://programmers.co.kr/learn/courses/30/lessons/60057
'''
def solution(s):
    answer = float('inf')
    if len(s)==1:
        return 1
    for i in range(1,len(s)//2+1):
        res = ''
        now=0
        cnt = 0
        temp = s[:i]
        while now<len(s):
            if temp==s[now:now+i]:
                cnt += 1
                now += i
                continue
            else:
                if cnt>1:
                    res += str(cnt) + temp
                else:
                    res += temp
                temp = s[now:now + i]
                now += i
                cnt = 1
        if cnt > 1:
            res += str(cnt) + temp
        else:
            res += temp
        answer = min(answer, len(res))
        # print(res)
    return answer


# print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
print(solution("a"))
# print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))