'''
SEA
벽돌깨기
모의 SW 역량테스트
50분
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo
'''
import sys
sys.stdin = open('sample_input.txt', 'r')

import copy
di = [-1,1,0,0]
dj = [0,0,-1,1]

def solve(dep, arr):
    global ans
    if dep == N:
        cnt = 0
        for i in range(H):
            for j in range(W):
                if arr[i][j] != 0:
                    cnt += 1
        ans = min(ans, cnt)
        return

    # 구슬을 쏘는 경우의 수
    for c in range(W):
        arr2 = copy.deepcopy(arr)
        # 구슬을 쐈을 때 제거되는 범위
        idx = 0
        while idx < H-1 and arr[idx][c] == 0:
            idx += 1

        q = []
        q.append([idx,c])
        while q:
            i, j = q.pop(0)
            power = arr2[i][j]
            arr2[i][j] = 0
            for k in range(1,power):
                for n in range(4):
                    ni, nj = i + k*di[n], j + k*dj[n]
                    if 0<=ni<H and 0<=nj<W and arr2[ni][nj] != 0:
                        q.append([ni,nj])

        # 남은 벽돌 아래로 이동
        for j in range(W):
            for i in range(H-1, 0, -1):
                if arr2[i][j] == 0:
                    ui = i - 1
                    while ui > 0 and arr2[ui][j] == 0:
                        ui -= 1
                    arr2[i][j], arr2[ui][j] = arr2[ui][j], arr2[i][j]

        solve(dep+1, arr2)

T = int(input())
for test_case in range(1,T+1):
    N, W, H = map(int, input().split())
    arr = []
    ans = 0 # 남은 벽돌의 갯수 구하기
    for i in range(H):
        arr.append(list(map(int, input().split())))
        for j in range(W):
            if arr[i][j] != 0:
                ans += 1
    solve(0, arr)
    print(f'#{test_case} {ans}')