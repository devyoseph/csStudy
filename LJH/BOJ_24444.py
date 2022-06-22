'''
BOJ
알고리즘 수업 - 너비 우선 탐색 1
실버 2
10분
https://www.acmicpc.net/problem/24444
'''
from collections import deque

N, M, R = map(int, input().split())
lst = [[] for _ in range(N+1)]
visited = [0]*(N+1)


for _ in range(M):
    u,v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)

for i in range(1,N+1):
    lst[i].sort()

queue = deque()
queue.append(R)
visited[R] = 1
cnt = 2
while queue:
    s = queue.popleft()
    for i in lst[s]:
        if visited[i] == 0:
            queue.append(i)
            visited[i] = cnt
            cnt += 1
for i in range(1,N+1):
    print(visited[i])