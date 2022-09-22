"""
BOJ
특정한 최단 경로
골드4
1시간~
https://www.acmicpc.net/problem/1504
"""
from collections import deque
def Dijkstra(start,end):
    V = [INF]*(N+1)
    Q = deque()
    V[start] = 0
    Q.append(start)
    while Q:
        v = Q.popleft()
        if v == end:
            return V[v]
        for next in graph[v]:
            if V[next[0]] > next[1] + V[v]:
                V[next[0]] = next[1] + V[v]
                Q.append(next[0])
    return V[end]

# 입력 받기
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
for i in range(N+1):
    graph[i].sort(key=lambda x:x[0])
    # print(graph[i])
V1, V2 = map(int, input().split())

INF = 1000*1000

path1 = Dijkstra(1,V1) + Dijkstra(V1,V2) + Dijkstra(V2,N)
path2 = Dijkstra(1,V2) + Dijkstra(V2,V1) + Dijkstra(V1,N)
res = min(path1,path2)
if res >= INF:
    print(-1)
else:
    print(res)
