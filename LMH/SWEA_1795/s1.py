import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

INF = float("inf")

def dijkstra(end, graph):
    D = [INF]*(N+1)
    D[end] = 0
    Q = deque()
    Q.append(end)
    while Q:
        node = Q.popleft()
        for next, w in graph[node]:
            d = D[node] + w
            if D[next] > d:
                D[next] = d
                Q.append(next)
    return D[1:]


T = int(input())
for test_case in range(1,T+1):
    N, M, X = map(int, input().split()) # 집의 수, 도로의 수, 인수의 집
    '''
    X번 집으로 오고 가는데 드는 시간 중에서 가장 오래 걸리는 집은 얼마나 걸리는지 구하기
    '''
    go = [[] for _ in range(N+1)]       # 가중치가 있는 단방향 그래프
    come = [[] for _ in range(N+1)]     # 가중치가 있는 단방향 그래프
    for _ in range(M):
        x, y, c = map(int, input().split())
        go[y].append([x,c])           # 생일 파티 갈 때
        come[x].append([y,c])         # 집에 돌아올 때

    res = 0
    for a, b in zip(dijkstra(X,go), dijkstra(X,come)):
        res = max(res,a+b)

    print(f'#{test_case} {res}')