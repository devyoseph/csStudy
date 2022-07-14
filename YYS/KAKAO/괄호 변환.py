def solution(p):

    # 완벽한 문자인지 검사
    def isPerfect(p):
        global letter_perfect, max_index

        # 올바른(완벽한) 괄호 문자열
        letter_perfect = True

        cnt = 0  # ( = 1 , ) = -1
        index = -1
        max_index = 0

        for letter in p:
            index += 1
            if letter == '(':
                cnt += 1
            else:
                cnt -= 1

            if cnt < 0:  # 한 번이라도 0보다 작아졌다면 완벽한 문자열은 아니다.
                return False

        if cnt != 0:
            return False

        return True

    # U를 구하는 메서드
    def getU(p):
        global max_index

        cnt = 0
        index = -1

        for letter in p:
            index += 1
            if letter == '(':
                cnt += 1
            else:
                cnt -= 1

            if cnt == 0:
                return p[0:index+1]

        return p[:-1]
    
    # u를 변형시켜주는 메서드
    def reverse_letter(u):
        # print("뒤집기전", u)
        u = u[1:len(u)-1]
        # print("잘랐다", u)
        res = ''
        for letter in u:
            # print(letter=="(")
            if letter == "(":
                res += ")"
            else:
                res += "("
        # print("뒤집은 후", res)
        return res

    def recursive(w):
        if isPerfect(w):
            return w

        u = getU(w)
        v = w[len(u):]

        if isPerfect(u):
            u += recursive(v)
            return u
        else:
            return "("+recursive(v)+")"+reverse_letter(u)

    return recursive(p)

#print(solution("(()())()"))
#print(solution(")("))
#print(solution("()))((()"))
