"""
BOJ
테트로미노
골드5
40분
https://www.acmicpc.net/problem/14500
"""
#pypy3 제출

### 특정 좌표로부터 dfs를 거리 3까지만 돌면
### ㅗ 모양을 제외한 모든 테트로미노를 만들 수 있다.
def dfs(r,c,dep,res):
    global ans
    if dep == 3:
        ans = max(ans, res)
        return
    for k in range(4):
        nr = r + di[k]
        nc = c + dj[k]
        if 0<=nr<N and 0<=nc<M and not visited[nr][nc]:
            #==================================== (1340ms)
            if dep == 1: # ㅗ,ㅓ,ㅏ,ㅜ 검사
                visited[nr][nc] = True
                dfs(r,c,dep+1,res+arr[nr][nc])
                visited[nr][nc] = False
            # ====================================
            visited[nr][nc] = True
            dfs(nr,nc,dep+1,res+arr[nr][nc])
            visited[nr][nc] = False

# ### ㅗ 모양 직접 체크 (872ms)
# def check(r,c):
#     global ans
#     #ㅗ
#     if 0 <= r - 1 < N and 0 <= (c - 1) and (c + 1) < M:
#         res = arr[r - 1][c] + arr[r][c - 1] + arr[r][c] + arr[r][c + 1]
#         ans = max(ans, res)
#     #ㅜ
#     if 0 <= r + 1 < N and 0 <= (c - 1) and (c + 1) < M:
#         res = arr[r + 1][c] + arr[r][c - 1] + arr[r][c] + arr[r][c + 1]
#         ans = max(ans, res)
#     #ㅓ
#     if 0 <= c - 1 < M and 0 <= (r - 1) and (r + 1) < N:
#         res = arr[r][c - 1] + arr[r - 1][c] + arr[r][c] + arr[r + 1][c]
#         ans = max(ans, res)
#     #ㅏ
#     if 0 <= c + 1 < M and 0 <= (r - 1) and (r + 1) < N:
#         res = arr[r][c + 1] + arr[r - 1][c] + arr[r][c] + arr[r + 1][c]
#         ans = max(ans, res)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
di = [0,0,-1,1]
dj = [-1,1,0,0]

ans = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i,j,0,arr[i][j])
        # check(i,j)
        visited[i][j] = False

print(ans)