"""
BOJ
신나는 함수 실행
실버2
40분
https://www.acmicpc.net/problem/9184
"""
MAX = 20 + 1
dp = [[[0]*MAX for _ in range(MAX)]for _ in range(MAX)]
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        dp[20][20][20] = w(20,20,20)
        return dp[20][20][20]
    elif dp[a][b][c] != 0: # 인덱스 에러 방지하기 위해 위에서 인덱스값 검사한 후 dp 에 값이 있는지 확인해야 한다.
        return dp[a][b][c]
    elif a < b < c:
        dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')