import sys
from collections import deque

sys.stdin = open("input.txt", "r")


def findend():
    for i in range(N):
        for j in range(M):
            if lst[i][j]==3:
                return (i,j)


def bfs(dif):
    dr = [0, 0]
    dc = [-1, 1]
    visited = [[0]*M for _ in range(N)]
    queue = []
    queue.append((er,ec))
    for i in range(1, dif + 1):
        dr += [-1 * i, 1 * i]
        dc += [0, 0]
    while queue:
        rr, cc = queue.pop(0)
        visited[rr][cc]=1
        for delta in range(len(dr)):
            nr = rr + dr[delta]
            nc = cc + dc[delta]
            if 0 <= nr < N and 0 <= nc < M and lst[nr][nc]!=0 and visited[nr][nc]==0:
                if lst[nr][nc] == 1:
                    queue.append((nr,nc))
                elif lst[nr][nc]==2:
                    return False
    return True


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    er, ec = findend()
    dif = N-er-1
    while dif>=1:
        if bfs(dif):
            break
        dif -= 1

    print(f'#{tc} {dif+1}')
