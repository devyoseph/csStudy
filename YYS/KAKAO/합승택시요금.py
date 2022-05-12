from pprint import pprint


def solution(n, s, a, b, fares):
    arr = [[float("inf") for _ in range(n)] for __ in range(n)]
    lst = [list() for _ in range(n)]

    for i in range(n):
        arr[i][i] = 0

    for f in fares:
        A = f[0] - 1
        B = f[1] - 1
        C = f[2]
        arr[A][B] = C
        arr[B][A] = C

    # 플로이드 워샬: 경찰과 도둑
    for i in range(n):
        for j in range(n):
            if i == j: continue
            for k in range(n):
                if j == k: continue
                arr[j][k] = min(arr[j][i] + arr[i][k], arr[j][k])

    # s와 b의 그냥 합
    MIN = float("inf")
    #pprint(arr)
    for i in range(n):
        if arr[i][a-1] + arr[i][b-1] + arr[i][s-1] < MIN:
            MIN = arr[i][a-1] + arr[i][b-1] + arr[i][s-1]
            #print(i, MIN, a, b)

    return MIN

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
