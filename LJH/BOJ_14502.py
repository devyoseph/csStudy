import copy
from collections import deque

def sun(n):
    # for i in range(1<<n):     # 탐색 시간 낭비
    #     temp = deque()
    #     for j in range(n):
    #         if i&(1<<j):
    #             temp.append(j)
    #         if len(temp)>3:     # 가지치기1
    #             break
    end = len(lst0)
    for i in range(end):
        for j in range(i+1, end):
            for k in range(j+1, end):
                bfs([lst0[i],lst0[j], lst0[k]])

def bfs(k):
    global res
    templst = copy.deepcopy(lst)
    temp_lst2 = copy.deepcopy(lst2)
    cnt = len(lst0)-3
    for h in k:
        templst[h[0]][h[1]] = 1 # 벽 3개 1 표시
    while temp_lst2:
        r, c = temp_lst2.popleft()
        for delta in [(-1, 0),(1, 0),(0, 1),(0, -1)]:
            nr = r + delta[0]
            nc = c + delta[1]
            if 0<=nr<N and 0<=nc<M and templst[nr][nc]==0:
                templst[nr][nc] = 2
                cnt -= 1
                temp_lst2.append((nr,nc))
    if res<cnt:
        res = cnt


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
lst0 = deque()
lst2 = deque()
for i in range(N):
    for j in range(M):
        if lst[i][j]==0:
            lst0.append((i,j))
        elif lst[i][j]==2:
            lst2.append((i,j))

res = 0
sun(len(lst0))
# order = sun(len(lst0))
# for k in order:
#     bfs(k)
print(res)

