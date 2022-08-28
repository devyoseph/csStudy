# 문제1: 기지국 건설 (92점)

import sys
sys.stdin = open('sample_input_WH15_T4.txt','r')

def solve(si, sj, dep, cost):
    global res
    if dep == 4:
        # if cost > 1300:
        # for i in v:
        #     print(i)
        # print()
        cost_benefit = cost**2
        res = max(res,cost_benefit)
        return
    else:
        # if si%2 == 0:
        #     dist = ((0,-1),(0,1),(-1,0),(1,0),(-1,0),(1,0))
        # else:
        #     dist = ((0,-1),(0,1),(-1,0),(1,0),(-1,-1),(1,-1))
        if (sj % 2) == 0:
            dist = ((0,-1),(0,1),(-1,0),(1,0),(-1,-1),(-1,1))
        else:
            dist = ((0,-1),(0,1),(-1,0),(1,0),(1,-1),(1,1))

        for di,dj in dist:
            ni, nj = si + di, sj + dj
            if 0<=ni<H and 0<=nj<W and v[ni][nj]==0:
                v[ni][nj] = 1
                solve(ni, nj, dep+1, cost + arr[ni][nj])
                v[ni][nj] = 0

T = int(input())
for test_case in range(1,T+1):
    W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    v = [[0]*W for _ in range(H)]
    res = 0
    cell = []
    # if test_case != 1:
    #     continue
    for i in range(H):
        for j in range(W):
            if i == 1 and j == 2 and v[i][j] == 0:
                v[i][j] = 1
                solve(i, j, 1, arr[i][j])
                v[i][j] = 0
    print(f'#{test_case} {res}')