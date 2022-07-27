"""
BOJ
토마토
골드5
40분
https://www.acmicpc.net/problem/7576
"""
# 1  : 익은 토마토
# 0  : 익지 않은 토마토
# -1 : 토마토가 들어 있지 않은 칸
# M, N = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# di = [-1,1,0,0]
# dj = [0,0,-1,1]
# date = -1 # 토마토가 모두 익을 때까지의 최소 날짜
#
# # 상자에 들어 있는 토마토 위치 구하기
# tomato = []
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 1:
#             tomato.append((i,j))
#
# while tomato:
#     date += 1
#     # print(date)
#     # for t in range(N):
#     #     print(arr[t])
#     for tom in range(len(tomato)):
#         i, j = tomato.pop(0)
#         # print(i, j)
#         for dr, dc in zip(di,dj):
#             nr = i + dr
#             nc = j + dc
#             if 0<= nr < N and 0<= nc < M and arr[nr][nc] == 0: # 익지 않은 토마토 있는 경우
#                 arr[nr][nc] = 1
#                 tomato.append((nr,nc))
#
# # 토마토가 모두 익지 못하는 상황이면 -1을 출력
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 0:
#             date = -1
# print(date)

#####################
# deque 사용
# 일반적인 리스트의 pop 연산이 O(n)이 소요되는데 반해, deque는 O(1)로 접근 가능하다.
from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
di = [-1,1,0,0]
dj = [0,0,-1,1]
date = -1 # 토마토가 모두 익을 때까지의 최소 날짜

# 상자에 들어 있는 토마토 위치 구하기
tomato = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            tomato.append((i,j))

while tomato:
    date += 1
    # print(date)
    # for t in range(N):
    #     print(arr[t])
    for tom in range(len(tomato)):
        i, j = tomato.popleft()
        # print(i, j)
        for dr, dc in zip(di,dj):
            nr = i + dr
            nc = j + dc
            if 0<= nr < N and 0<= nc < M and arr[nr][nc] == 0: # 익지 않은 토마토 있는 경우
                arr[nr][nc] = 1
                tomato.append((nr,nc))

# 토마토가 모두 익지 못하는 상황이면 -1을 출력
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            date = -1
print(date)