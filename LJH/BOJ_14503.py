from collections import deque


def move():
    global cnt
    while queue:
        temp = queue.popleft()
        r, c, d = temp[0], temp[1], temp[2]
        if lst[r][c]==0:
            lst[r][c] = 2
            cnt += 1
        for delta in range(-1, -5, -1):     # 상우하좌가 0123에서 왼쪽 방향으로 향하게 -1씩
            nr = r + dr[(delta+d)%4]
            nc = c + dc[(delta+d)%4]
            if 0<=nr<N and 0<=nc<M and lst[nr][nc]==0:
                queue.append([nr,nc,(delta+d)%4])   # 다음 목적지 정해지면 break
                break
        else:
            br = r + dr[(d-2)%4]
            bc = c + dc[(d-2)%4]
            if 0<=br<N and 0<=bc<M and lst[br][bc]!=1:  # 청소할 곳 없고 후진 시 벽이 아닐 때
                queue.append([br, bc, d])
            else:           # 청소할 곳 없고 후진 못 할 때 종료
                return

N, M = map(int, input().split())
r, c, d = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
dr = [-1, 0, 1, 0] # 상우하좌
dc = [0, 1, 0, -1]
check = False   # 반복 중단용
cnt = 0
queue.append([r,c,d])
move()
print(cnt)