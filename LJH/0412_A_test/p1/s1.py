import copy
import sys
sys.stdin = open("input.txt", "r")

def dfs(n,r,c,cnt,tempvisited):
    global result
    tempvisited1 = copy.deepcopy(tempvisited)
    if cnt+(3-n)*maxval<result:
        return
    if n==3:
        result = max(result,cnt)
        return
    tempvisited1[r][c]=2
    templst = bfs(r,c)
    for nr,nc in templst:
        if tempvisited1[nr][nc]==0:
            tempvisited1[nr][nc]=1
    if n==2:
        maxv = 0
        for ii in range(H):
            for jj in range(W):
                if tempvisited1[ii][jj] == 1:
                    if maxv<lst[ii][jj]:
                        maxv = lst[ii][jj]
                        maxi = ii
                        maxj = jj
        dfs(n + 1, maxi, maxj, cnt + lst[maxi][maxj], tempvisited1)
    else:
        for ii in range(H):
            for jj in range(W):
                if tempvisited1[ii][jj]==1:
                    dfs(n+1,ii,jj,cnt+lst[ii][jj], tempvisited1)

def bfs(r,c):
    res = []
    for delta in range(6):
        if c % 2 == 0:
            nr = r + dr1[delta]
            nc = c + dc1[delta]
        elif c%2:
            nr = r + dr2[delta]
            nc = c + dc2[delta]
        if 0<=nr<H and 0<=nc<W:
            res.append((nr,nc))
    return res



dr1 = [0, 0, 1, -1, -1, -1] # w%2 == 0
dc1 = [1, -1, 0, 0, 1, -1]
dr2 = [0, 0, 1, -1, 1, 1]   # w%2 == 1
dc2 = [1, -1, 0, 0, 1, -1]
T = int(input())
for tc in range(1, T+1):
    W, H = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(H)]
    result = 0
    visited = [[0] * W for _ in range(H)]
    val = 0
    maxval = 0
    for i in lst:
        val += sum(i)
        maxval = max(maxval, max(i))
    val %= H*W
    for i in range(H):
        for j in range(W):
            if lst[i][j]>=val:
                dfs(0,i,j,lst[i][j],visited)
    print(f'#{tc} {result**2}')