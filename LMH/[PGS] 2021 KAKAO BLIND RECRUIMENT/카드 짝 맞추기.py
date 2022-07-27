"""
PGS
카드 짝 맞추기
level3
-
https://programmers.co.kr/learn/courses/30/lessons/72415
"""
# 참고한 코드
# https://velog.io/@rltjr1092/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B9%B4%EB%93%9C-%EC%A7%9D-%EB%A7%9E%EC%B6%94%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%92%80%EC%9D%B4
from math import inf
from copy import deepcopy
from collections import deque

answer = inf

def get_cnt(arr, si, sj, ei, ej):
    visited = [[inf] * 4 for _ in range(4)]
    q = deque()
    q.append([si, sj])
    visited[si][sj] = 0
    while q:
        i, j = q.popleft()

        if i == ei and j == ej:
            return visited[i][j]

        # 한칸씩 움직인 경우
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = i + di, j + dj
            if 0 <= ni < 4 and 0 <= nj < 4 and arr[ni][nj] and visited[ni][nj] > visited[i][j] + 1:
                visited[ni][nj] = visited[i][j] + 1
                q.append([ni, nj])

        # ctrl 키로 움직인 경우
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = i + di, j + dj
            while 0 <= ni + di < 4 and 0 <= nj + dj < 4 and arr[ni][nj] == 0:
                ni += di
                nj += dj
            if 0 <= ni < 4 and 0 <= nj < 4 and visited[ni][nj] > visited[i][j] + 1:
                visited[ni][nj] = visited[i][j] + 1
                q.append([ni, nj])


def get_coord_by_num(arr, target):
    for i in range(4):
        for j in range(4):
            if arr[i][j] == target:
                return i, j


def is_end(arr):
    for i in range(4):
        for j in range(4):
            if arr[i][j] != 0:
                return False
    return True


def solve(b_arr, si, sj, ti, tj, cnt):
    global answer

    arr = deepcopy(b_arr)
    target_num = arr[ti][tj]
    # 첫번째 카드 cnt
    cnt += get_cnt(arr, si, sj, ti, tj)
    arr[ti][tj] = 0

    # 두번째 카드 cnt
    tti, ttj = get_coord_by_num(arr, target_num)
    cnt += get_cnt(arr, ti, tj, tti, ttj)
    arr[tti][ttj] = 0
    cnt += 2  # enter 횟수 더하기

    # 모든 카드 다 찾았는지 검사
    if is_end(arr):
        answer = min(answer, cnt)
        return

    # 다음 카드 정하기
    for i in range(4):
        for j in range(4):
            if arr[i][j] != 0:
                solve(arr, tti, ttj, i, j, cnt)


def solution(board, r, c):
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                solve(board, r, c, i, j, 0)
    return answer

# print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))