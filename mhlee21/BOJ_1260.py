"""
BOJ
DFS와 BFS
실버2
60분
https://www.acmicpc.net/problem/1260
"""
def bfs(n):
    queue = []
    queue.append(n)
    visited[n] = True
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def dfs(n):
    print(n, end=' ')
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()


visited = [False]*(N+1)
dfs(V)
print()
visited = [False]*(N+1)
bfs(V)
