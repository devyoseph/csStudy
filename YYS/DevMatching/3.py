from copy import copy


def solution(k):
    # 4 , 2 , 5, 5, 4, 5, 6, 6, 4, 6, 6
    global number, count
    number = [6, 2, 5, 5, 4, 5, 6, 4, 3, 7, 6]
    count = 0
    # 중복 숫자..
    def dfs(depth, hubo, S):
        global count
        start = 0
        if depth == 0:
            start += 1
        for i in range(start, 10):
            if S >= number[i]:
                #print(i, S)
                dfs(depth + 1, hubo, S - number[i])

        if S < 2:
            if S == 0:
                #print(S)
                count += 1
            return

    dfs(0, list(), k)
    return count

print(solution(5))