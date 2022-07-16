'''
PGS
괄호 변환
lv 2
30분
https://school.programmers.co.kr/learn/courses/30/lessons/60058
'''

def solution(p):
    answer = ''
    def sol(p):
        if p == '':
            return ''
        u,v = '', ''
        a, b = 0,0
        res = 0
        flag = True
        for i in range(len(p)):
            if p[i]=='(':
                a += 1
                res += 1
            else:
                b += 1
                res -= 1
            if res<0:
                flag = False
            if a==b:
                u = p[:i+1]
                v = p[i+1:]
                break
        if not flag:
            nu = ''
            for i in range(1,len(u)-1):
                if u[i]=='(':
                    nu += ')'
                else:
                    nu += '('
            word = '(' + sol(v) + ')' + nu
        else:
            word = u + sol(v)
        return word

    answer = sol(p)
    return answer


# print(solution("(()())()"))
# print(solution(")("))
print(solution("()))((()"))