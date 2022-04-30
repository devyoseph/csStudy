from sys import stdin
from collections import deque
input = stdin.readline

def move(r,c,delta):
    cnt = 0
    while lst[r+dr[delta]][c+dc[delta]]!='#' and lst[r][c]!='O':
        r += dr[delta]
        c += dc[delta]
        cnt += 1
    return r,c,cnt

def bfs():
    queue = deque()
    queue.append((rs[0], rs[1], bs[0], bs[1], 1))
    visited[rs[0]][rs[1]][bs[0]][bs[1]]=1
    while queue:
        rr, rc, br, bc, d = queue.popleft()
        if d>=11:
            print(-1)
            return
        for i in range(4):
            nrr, nrc, mr = move(rr, rc, i)
            nbr, nbc, mb = move(br, bc, i)
            if lst[nbr][nbc]=='O':
                continue
            if lst[nrr][nrc]=='O':
                print(d)
                return
            if nrr==nbr and nrc==nbc:
                if mr>mb:
                    nrr -= dr[i]
                    nrc -= dc[i]
                else:
                    nbr -= dr[i]
                    nbc -= dc[i]
            if visited[nrr][nrc][nbr][nbc]==0:
                visited[nrr][nrc][nbr][nbc] = 1
                queue.append((nrr,nrc,nbr,nbc,d+1))
    print(-1)



dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

N, M = map(int, input().split())
lst = [list(input().strip()) for _ in range(N)]
visited = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if lst[i][j]=='R':
            rs = (i,j)
        elif lst[i][j]=='B':
            bs = (i,j)

bfs()