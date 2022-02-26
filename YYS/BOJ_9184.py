def w(a, b, c):
    global dp

    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    # if dp[a][b][c]:
    #     return dp[a][b][c]
    # if a < b < c:
    #     dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    #     return dp[a][b][c]
    # dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    # return dp[a][b][c]
    # 왜 실패한지 모르는 코드 : 해결 [[[None]*21]*21]*21 가 shallow copy
    if dp[a][b][c] is None:
        if a < b < c:
            dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        else:
            dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return dp[a][b][c]


dp = [[[None]*21 for i in range(21)] for j in range(21)]
while True:
    a, b, c = list(map(int, input().split())) # 변수 초기화 부분
    if a == b == c == -1: break

    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')
