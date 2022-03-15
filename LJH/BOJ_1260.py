
def dfs(start):
    visited[start] = 1
    print(start, end=' ')
    for i in lst[start]:
        if visited[i] == 0:
            dfs(i)

def bfs(start):
    while queue:
        a = queue.pop(0)
        if visited[a]==0:
            visited[a] = 1
            print(a, end=' ')
            for i in lst[a]:
                if visited[i]==0:
                    queue.append(i)



N, M, V = map(int, input().split())
lst = [[] for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    lst[i].append(j)
    lst[j].append(i)
for i in range(len(lst)):
    lst[i].sort()
visited = [0]*(N+1)
queue = [V]
dfs(V)
print()
visited = [0]*(N+1)
bfs(V)