from collections import deque

N, M, V = list(map(int, input().split()))
arr = [[False for i in range(N + 1)] for i in range(N + 1)]

# 인접행렬로 연결하기
for i in range(M):
    a, b = list(map(int, input().split()))
    arr[a][b] = True
    arr[b][a] = True

def dfs(v):
    global visit, answer

    visit[v] = True

    answer.append(v)

    for i in range(1, N + 1):
        if not visit[i] and arr[v][i]:
            dfs(i)

def bfs(v):
    global visit,answer
    q = deque()
    q.append(v)
    visit[v] = True
    answer.append(v)

    while len(q)!=0:
        now = q.popleft()
        for i in range(1,N+1):
            if not visit[i] and arr[now][i]:
                visit[i] = True
                answer.append(i)
                q.append(i)

visit = [False] * (N + 1)
answer = []
dfs(V)
print(*answer)
visit = [False] * (N + 1)
answer = []
bfs(V)
print(*answer)
