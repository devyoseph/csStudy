import sys
input = sys.stdin.readline
def dijkstra(start):
    D = [INF] * (N + 1)
    U = [start]
    D[start]=0
    for i in range(N+1):
        if lst[start][i]:
            D[i] = min(D[i], lst[start][i])
    while V!=sorted(U):
        mind = INF
        for i in range(N + 1):
            if i not in U and mind>D[i]:
                mind = D[i]
                mini = i
        U.append(mini)
        for i in range(N + 1):
            if lst[mini][i]:
                D[i] = min(D[i], mind + lst[mini][i])
    return D

N, E = map(int, input().split())
INF = float('inf')
lst = [[0]*(N+1) for _ in range(N+1)]
for i in range(N+1):
    lst[i][i] = 0
for _ in range(E):
    a, b, c = map(int, input().split())
    lst[a][b] = c
    lst[b][a] = c
v1, v2 = map(int, input().split())
# for k in range(1,N+1):
#     for r in range(1, N + 1):
#         for c in range(1, N + 1):
#             lst[r][c] = min(lst[r][c], lst[r][k] + lst[k][c])
# result = min(lst[1][v1]+lst[v1][v2]+lst[v2][N], lst[1][v2]+lst[v2][v1]+lst[v1][N])
#
# if result==INF:
#     result = -1
# print(result)

INF = float('inf')
V = [i for i in range(1,N+1)]
a = dijkstra(1)
b = dijkstra(v1)
c = dijkstra(N)
aa = a[v1] + b[v2] + c[v2]
bb = a[v2] + b[v2] + c[v1]
print(min(aa,bb))

