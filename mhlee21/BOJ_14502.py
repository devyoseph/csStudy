"""
BOJ
연구소
골드5
2시간 30분
https://www.acmicpc.net/problem/14502
"""
import copy
from collections import deque
import sys

def bfs():
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    q = deque()
    for v in virus:
        q.append(v)
    visited = copy.deepcopy(arr)
    area = start
    while q:
        i, j = q.popleft()
        for di,dj in zip(dr,dc):
            r, c = i + di, j + dj
            if 0<=r<N and 0<=c<M and visited[r][c] == 0:
                visited[r][c] = 2
                area -= 1
                q.append((r,c))
    return area

def solve(n, row):
    global safe_area
    if n == 3:
        area = bfs()
        safe_area = max(safe_area, area)
        return

    # for 문의 row 범위를 0~N으로 해도 되지만 시간초과가 발생한다.
    # 중복 검사하는 문제를 해결하기 위해 이전값은 검사하지 않도록 했다.
    for i in range(row,N):
        for j in range(0,M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                solve(n+1, i)
                arr[i][j] = 0

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
safe_area = 0
start = -3
virus = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus.append((i, j))
        if arr[i][j] == 0:
            start += 1
solve(0, 0)
print(safe_area)