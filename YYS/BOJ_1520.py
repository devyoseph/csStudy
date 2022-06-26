M, N = map(int, input().split())
arr = list()
dp = [[-1 for _ in range(N)] for __ in range(M)]
count = 0
for m in range(M):
    temp = list(map(int, input().split()))
    arr.append(temp)
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def dfs(row, col, arr, dp):
    global dx, dy, M, N, count
    dp[row][col] = 1
    now = arr[row][col]

    if row == M-1 and col == N-1:
        return 1

    for k in range(4):
        r = row + dx[k]
        c = col + dy[k]

        if r<0 or r>=M or c<0 or c>=N or now>=arr[r][c]:
            continue
        
        if dp[r][c] == -1:
            dp[r][c] = dfs(r,c,arr,dp)
        elif dp[r][c] == 1:
            count += 1
            return 1

dfs(M-1, N-1, arr, dp)
print(count)
        