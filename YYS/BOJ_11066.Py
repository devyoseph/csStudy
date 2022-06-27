T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [[0]*N for _ in range(N)]

    for i in range(2, N+1): # 길이: 2~N
        for j in range(N-i+1): # 시작점: j, 길이: i, 끝점: j+i-1, 범위: < N-1
            dp[j][j+i-1] = min(dp[j][j+n] + dp[j+n+1][j+i-1] for n in range(i-1)) + sum(arr[j:j+i])
    print(dp[0][N-1])