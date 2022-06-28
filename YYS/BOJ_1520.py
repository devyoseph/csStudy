M, N = map(int, input().split())
arr = list()
dp = [[-1 for _ in range(N)] for __ in range(M)]
dp[M-1][N-1] = 1 # 정답으로 이어진 길
count = 0

# 입력값
for m in range(M):
    temp = list(map(int, input().split()))
    arr.append(temp)

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def dfs(row, col, arr, dp):
    global dx, dy, M, N, count
    #print(row,col)

    if dp[row][col] != -1:
        count += dp[row][col]
        return dp[row][col]

    elif dp[row][col] == -1: # 현재 위치 탐색 X
        dp[row][col] = 0 # 방문체크
        now = arr[row][col] # 현재 위치 배열값
        tmp = 0
        for k in range(4):
            r = row + dx[k]
            c = col + dy[k]

            if r<0 or r>=M or c<0 or c>=N or now<=arr[r][c]:
                continue

            tmp += dfs(r,c,arr,dp)
            dp[row][col] = tmp

    return dp[row][col]

dfs(0, 0, arr, dp)
#print(dp)
print(count)
        