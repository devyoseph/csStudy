from collections import deque

def bfs(arr, visit, res, R):
    number = 1

    dq = deque()
    visit[R] = True
    dq.append(R)

    while len(dq):
        now = dq.pop()
        res[now] = number
        number = number + 1
        
        for x in arr[now]:
            if not visit[x]:
                visit[x] = True
                dq.appendleft(x)
                

N, M, R = map(int, input().split())
arr = [list() for _ in range(N)]
res = [0]*N # 결과 저장
visit = [False]*N

for _ in range(M):
    a, b = map(int, input().split())
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)

for a in arr:
    a.sort();

bfs(arr, visit, res, R-1)

for i in range(N):
    print(res[i])