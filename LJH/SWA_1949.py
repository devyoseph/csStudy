import sys
sys.stdin = open("sample_input.txt", "r")

def bfs(r,c, cnt,can):
    global res
    visited[r][c]=1
    for delta in range(4):
        nr = r + dr[delta]
        nc = c + dc[delta]
        if 0<=nr<N and 0<=nc<N and visited[nr][nc]==0 and lst[nr][nc]<lst[r][c]:
            bfs(nr,nc,cnt+1,can)
            visited[nr][nc]=0
        elif can==0 and 0<=nr<N and 0<=nc<N and visited[nr][nc]==0 and lst[nr][nc]-K<lst[r][c]:
            temp = lst[nr][nc]
            lst[nr][nc] = lst[r][c]-1
            bfs(nr,nc,cnt+1,1)
            visited[nr][nc] = 0
            lst[nr][nc]=temp

    res = max(res, cnt)
    return


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    mh = 0
    res = 0
    for r in range(N):
        for c in range(N):
            if lst[r][c]>mh:
                mh = lst[r][c]
    for r in range(N):
        for c in range(N):
            if lst[r][c]==mh:
                bfs(r,c,1,0)
                visited[r][c] = 0

    print(f'#{tc} {res}')