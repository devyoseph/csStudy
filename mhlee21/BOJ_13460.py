"""
BOJ
구슬 탈출 2
골드1
3시간
https://www.acmicpc.net/problem/13460
"""
from collections import deque

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]

red = blue = (0,0)
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'R':
            red = i,j
        elif graph[i][j] == 'B':
            blue = i,j

di = [0,0,1,-1]
dj = [1,-1,0,0]
def bfs():
    visited = []
    visited.append([red[0],red[1],blue[0],blue[1]])
    Q = deque()
    Q.append([1, red[0],red[1],blue[0],blue[1]])
    while Q:
        cnt, ri, rj, bi, bj = Q.popleft()
        if cnt > 10:
            return -1
        for k in range(4):  # 방향별 체크
            rcnt = 0
            nri, nrj = ri, rj
            while True:
                if graph[nri + di[k]][nrj + dj[k]] == '#':
                    break
                if graph[nri][nrj] == 'O':
                    break
                nri += di[k]
                nrj += dj[k]
                rcnt += 1

            bcnt = 0
            nbi, nbj = bi, bj
            while True:
                if graph[nbi + di[k]][nbj + dj[k]] == '#':
                    break
                if graph[nbi][nbj] == 'O':
                    break
                nbi += di[k]
                nbj += dj[k]
                bcnt += 1

            # if [ri,rj,bi,bj] == [nri,nrj,nbi,nbj]:
            #     continue
            if graph[nbi][nbj] == 'O':
                continue
            elif graph[nri][nrj] == 'O':
                return cnt

            if nri == nbi and nrj == nbj:
                if rcnt > bcnt:
                    nri -= di[k]
                    nrj -= dj[k]
                else:
                    nbi -= di[k]
                    nbj -= dj[k]

            if [nri,nrj,nbi,nbj] in visited:
                continue
            else:
                visited.append([nri,nrj,nbi,nbj])
                Q.append([cnt+1,nri,nrj,nbi,nbj])
    return -1

res = bfs()
print(res)