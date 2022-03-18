from collections import deque

M, N = list(map(int, input().split()))
arr = []
start = []  # 시작 토마토 위치
cnt = 0
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(M):
        if lst[j] == 1:
            start.append([i, j])
        elif not lst[j]:
            cnt += 1
    arr.append(lst)

# 방향좌표
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

max = 0;


def bfs():
    global start, M, N, arr, max, cnt
    q = deque()
    for s in start:
        q.append(s)

    while len(q) != 0:

        now = q.popleft()
        row = now[0]
        col = now[1]

        for k in range(4):
            r = row + dx[k]
            c = col + dy[k]
            # 가지치기
            if r < 0 or r >= N or c < 0 or c >= M or arr[r][c]:
                continue
            cnt -= 1
            arr[r][c] = arr[row][col] + 1
            max = arr[r][c]
            q.append([r, c])


bfs()
if cnt>0:
    print(-1)
elif not max:
    print(0)
else:
    print(max-1)
