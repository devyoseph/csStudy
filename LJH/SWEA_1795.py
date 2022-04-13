# import sys
# sys.stdin = open("input.txt", "r")
#
# T = int(input())
# for tc in range(1, T+1):
#     N,M,X = map(int, input().split())
#     INF = float('inf')
#     lst = [[INF]*(N) for _ in range(N)]
#     for i in range(N):
#         lst[i][i]=0
#     for _ in range(M):
#         x, y, c = map(int, input().split())
#         lst[x-1][y-1] = c
#     for k in range(N):
#         for r in range(N):
#             for c in range(N):
#                 lst[r][c] = min(lst[r][c], lst[r][k]+lst[k][c])
#     result = 0
#     for i in range(N):
#         if i!=X:
#             result = max(result, lst[X-1][i]+lst[i][X-1])
#     print(f'#{tc} {result}')

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    lst = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        lst[x][y] = c
    Dijkstra(X)
    print(f'#{tc} {}')