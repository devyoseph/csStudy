# 문제2: 암벽 등반 (100점)

import sys
from pprint import pprint
sys.stdin = open('sample_input.txt','r')
from collections import deque

def solve(si,sj,ei,ej):
    v = [[0]*M for _ in range(N)]
    Q = deque()
    Q.append([si,sj])
    v[si][sj] = 1
    while Q:
        i, j = Q.popleft()
        # 양 옆으로 이동하는 경우
        for di, dj in ((0,-1),(0,1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj]:
                if v[ni][nj] == 0 or v[ni][nj] > v[i][j]:
                    v[ni][nj] = v[i][j]
                    Q.append([ni,nj])
        # 위아래로 이동하는 경우
        for di, dj in ((-1,0), (1,0)):
            ni, nj = i + di, j + dj
            height = 1
            while 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0:
                    ni += di
                    height += 1
                else:
                    if v[ni][nj] == 0 or v[ni][nj] > v[i][j]:
                        v[ni][nj] = max(v[i][j],height)
                        Q.append([ni,nj])
                    break
        # pprint(v)
        # print(Q)
    return v[ei][ej]

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    si=sj=ei=ej=0
    # if test_case != 1:
    #     continue
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                si, sj = i, j
            elif arr[i][j] == 3:
                ei, ej = i, j
    # level = 0
    # print(si, sj, ei, ej)
    res = solve(si,sj,ei,ej)
    print(f'#{test_case} {res}')