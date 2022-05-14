'''
PGS
합승 택시 요금
lv 3
40분
https://programmers.co.kr/learn/courses/30/lessons/72413
'''
def solution(n, s, a, b, fares):
    INF = float('inf')
    lst = [list(INF for _ in range(n)) for _ in range(n)]
    for fare in fares:
        lst[fare[0]-1][fare[1]-1] = fare[2]
        lst[fare[1] - 1][fare[0] - 1] = fare[2]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i==j:
                    lst[i][j]=0
                    continue
                if lst[i][j]>lst[i][k] + lst[k][j]:
                    lst[i][j] = lst[i][k] + lst[k][j]
    res = [0]*n
    for i in range(n):
        res[i] = lst[s-1][i] + lst[i][a-1] + lst[i][b-1]

    answer = min(res)
    return answer


print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))