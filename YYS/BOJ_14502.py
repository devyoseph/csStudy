import copy
from collections import deque

# 설계 내용
# 1. N,M 8칸 = 64 경우의 수 = (64x63x62)/(3x2) = 31x21x64 = 36000
# 2. 0을 모두 후보에 넣고 백트래킹 방식 or 브루트 포스 depth 3

N, M = list(map(int, input().split()))

visit = []  # Boolean 배열만 사용
start = []  # 바이러스 시작점 기록
cnt = -3  # 0의 개수를 세어줌, 나중에 어차피 3을 빼므로 미리 뺸다

for i in range(N):
    arr = list(map(int, input().split()))
    visit.append([False] * M)  # 맞는지 확인
    for j in range(M):
        if arr[j] == 2:
            start.append([i, j])
            visit[i][j] = True
        elif arr[j] == 1:
            visit[i][j] = True
        elif arr[j] == 0:
            cnt += 1

depth = 0  # 기준 깊이

# 일단 벽 3개 선택 메서드
temp = []
MAX = 0
# 방향 배열
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


# BFS 활용
def spread(arr):
    global cnt, start, dx, dy, MAX
    count = cnt  # 세어줄 임시 count
    q = deque()

    for s in start:
        q.append(s)

    while len(q) != 0:
        now = q.popleft()
        row = now[0]
        col = now[1]
        arr[row][col] = True
        for i in range(4):
            r = row + dx[i]
            c = col + dy[i]

            # 가지치기
            if r < 0 or r >= N or c < 0 or c >= M or arr[r][c]:
                continue

            count -= 1
            arr[r][c] = True
            q.append([r, c])
    MAX = max(MAX, count)

# 스도쿠 원리 이용
def select(depth, row, col):
    global visit, cnt, temp
    if depth == 3:
        spread(copy.deepcopy(visit))
        return

    if col >= M:
        col = 0
        row += 1
    if row >= N:
        return

    if visit[row][col]:
        select(depth, row, col + 1)
    else:
        visit[row][col] = True
        select(depth + 1, row, col + 1)
        visit[row][col] = False
        select(depth, row, col + 1)

select(0, 0, 0)
print(MAX)
