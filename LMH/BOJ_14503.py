"""
BOJ
로봇청소기
골드5
40분
https://www.acmicpc.net/problem/14503
"""
def solve(r,c,d):
    global cnt
    dist = [(-1,0), (0,1), (1,0), (0,-1)] # 북(0), 동(1), 남(2), 서(3)

    if arr[r][c] == 0:
        arr[r][c] = 2 # 현재 위치를 청소한다.
        cnt += 1
    for _ in range(4):
        d = (d -1 + 4) % 4 # 현재 방향을 기준으로 왼쪽 방향을 탐색하기 위함
        dr, dc = r + dist[d][0], c + dist[d][1]
        if arr[dr][dc] == 0: # 아직 청소하지 않은 공간이 남아있다면
            solve(dr,dc,d)
            return
    else: # 네 방향 모두 청소가 되어있거나, 벽인 경우
        dr, dc = r - dist[d][0], c - dist[d][1] # 바라보는 방향 유지한채로 한칸 후진
        if arr[dr][dc] == 1: # 뒤가 벽이라 후진할 수 없는 경우
            return
        solve(dr,dc,d)

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
cnt = 0

solve(r,c,d)
print(cnt)