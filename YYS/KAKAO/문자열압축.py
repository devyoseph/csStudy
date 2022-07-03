def solution(s):
    global MIN
    LENGTH = len(s)
    MAX_LENGTH = len(s)//2

    MIN = LENGTH

    for i in range(1, MAX_LENGTH+1): # i: 현재 검사 길이
        index = i
        numbering = 0

        arr = [0]*(LENGTH//i)
        arr[0] = 1

        while i+index < LENGTH+1:
            if s[index-i:index] != s[index:index+i]:
                numbering += 1
            arr[numbering] += 1
            index += i

        # 계산 부분
        SUM = LENGTH % i
        for a in arr:
            if a == 0: # 없다면 더하지 않고
                continue
            elif a == 1: # 1이면 굳이 숫자를 써주지 않고
                SUM += i
            else: # 2 이상이면 숫자 + 문자열길이= = 1 + i
                SUM += i + len(str(a))

        if MIN > SUM:
            MIN = SUM

    # print(MIN)

    return MIN