"""
BOJ
알고리즘 수업 - 깊이 우선 탐색 1
실버 2
50분
https://www.acmicpc.net/problem/24479
"""
#pypy3 제출

import sys
sys.setrecursionlimit(100000)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)

def dfs(node):
    global cnt
    visited[node] = cnt
    cnt += 1
    for next in graph[node]:
        if visited[next] == 0:
            dfs(next)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,N+1):
    graph[i].sort()

cnt = 1
dfs(R)
for i in visited[1:]:
    print(i)