from collections import deque


M, N = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
deq = deque()
result = -1     # 모두 익지는 못하는 상황이면 -1
for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            deq.append([i,j,0])
# visited = [[0]*M for _ in range(N)]
while deq:
    temp = deq.popleft()
    # if visited[temp[0]][temp[1]]==0:
    # visited[temp[0]][temp[1]] = 1
    for delta in range(4):
        nr = temp[0]+dr[delta]
        nc = temp[1]+dc[delta]
        if 0<=nr<N and 0<=nc<M and lst[nr][nc]==0:
            lst[nr][nc] = 1
            deq.append([nr,nc,temp[2]+1])
    if not deq:
        for ls in lst:
            if 0 in ls:
                result = -1
                break
        else:
            result = temp[2]
print(result)