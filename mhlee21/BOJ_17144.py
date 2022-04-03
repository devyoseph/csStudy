"""
BOJ
미세먼지 안녕!
골드4
1시간
https://www.acmicpc.net/problem/17144
"""
# pypy3 로 제출
from collections import deque

def diffusion():
    while dust:
        r, c, dnum = dust.popleft()
        fine_dust = dnum//5
        for di,dj in dust_dir:
            i = r + di
            j = c + dj
            if 0<=i<R and 0<=j<C and [i,j] not in air_cleaner:
                arr[i][j] += fine_dust
                arr[r][c] -= fine_dust

def cleaning():
    dir1 = dir2 = 0
    r1, c1 = air_cleaner[0]
    r2, c2 = air_cleaner[1]
    r1 += air_dir1[dir1][0]
    c1 += air_dir1[dir1][1]
    r2 += air_dir2[dir2][0]
    c2 += air_dir2[dir2][1]
    next1 = next2 = 0
    while True:
        # print(r1,c1,r2,c2)
        if arr[r1][c1] == -1 and arr[r2][c2] == -1:
            return
        # 위쪽 공기 청정기
        if arr[r1][c1] != -1:
            next1, arr[r1][c1] = arr[r1][c1], next1
            r1 += air_dir1[dir1][0]
            c1 += air_dir1[dir1][1]
            if 0 > r1 or r1 >= R or 0 > c1 or c1 >= C:
                r1 -= air_dir1[dir1][0]
                c1 -= air_dir1[dir1][1]
                dir1 = (dir1+1)%4
                r1 += air_dir1[dir1][0]
                c1 += air_dir1[dir1][1]
        # 아래쪽 공기청정기
        if arr[r2][c2] != -1:
            next2, arr[r2][c2] = arr[r2][c2], next2
            r2 += air_dir2[dir2][0]
            c2 += air_dir2[dir2][1]
            if 0 > r2 or r2 >= R or 0 > c2 or c2 >= C:
                r2 -= air_dir2[dir2][0]
                c2 -= air_dir2[dir2][1]
                dir2 = (dir2 + 1) % 4
                r2 += air_dir2[dir2][0]
                c2 += air_dir2[dir2][1]

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
dust_dir = ((-1,0),(1,0),(0,-1),(0,1)) # 상 하 좌 우
air_dir1 = ((0,1),(-1,0),(0,-1),(1,0)) # 우 상 좌 하
air_dir2 = ((0,1),(1,0),(0,-1),(-1,0)) # 우 하 좌 상

# 공기 청정기, 미세먼지 위치 구하기
air_cleaner = []
dust = deque()
for i in range(R):
    for j in range(C):
        if arr[i][j] == -1: # 공기 청정기 위치
            air_cleaner.append([i,j])
        elif arr[i][j] != 0: # 미세먼지 위치
            dust.append([i,j,arr[i][j]])

for sec in range(T): # T초 동안 미세먼지확산, 공기청정
    diffusion()
    cleaning()
    # for i in range(R):
    #     print(arr[i])
    cnt = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                dust.append([i,j,arr[i][j]])
                cnt += arr[i][j]

print(cnt)