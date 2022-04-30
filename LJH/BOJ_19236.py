import copy

def fish_move(flst,i):
    for r in range(4):
        for c in range(4):
            if flst[r][c][0] == i:
                for delta in range(8):
                    nr = r + dr[(flst[r][c][1] + delta) % 8]
                    nc = c + dc[(flst[r][c][1] + delta) % 8]
                    if 0 <= nr < 4 and 0 <= nc < 4 and flst[nr][nc][0] != -1:
                        flst[r][c][1] = (flst[r][c][1] + delta) % 8
                        flst[r][c], flst[nr][nc] = flst[nr][nc], flst[r][c]
                        return

def shark_move(lst,cnt,sr,sc):
    global res
    # 물고기 이동
    tlst = copy.deepcopy(lst)
    for i in range(1, 17):
        fish_move(tlst,i)
    # 상어 이동 가능한 곳 탐색
    movelst = []
    for i in range(1, 4):
        nr = sr + dr[tlst[sr][sc][1]] * i
        nc = sc + dc[tlst[sr][sc][1]] * i
        if 0 <= nr < 4 and 0 <= nc < 4 and tlst[nr][nc][0] != 0:
            movelst.append([nr, nc])
    # 이동 가능한 곳 없으면 종료
    if not movelst:
        res = max(res, cnt)
        return
    # 이동 가능한 곳으로 dfs
    for i in range(len(movelst)):
        temp = tlst[movelst[i][0]][movelst[i][1]]   # 되돌릴 먹이 생선
        temp_shark_dir = tlst[sr][sc][1]            # 되돌릴 상어 방향
        tlst[sr][sc][1] = tlst[movelst[i][0]][movelst[i][1]][1]     # 상어방향 미리 변경
        tlst[movelst[i][0]][movelst[i][1]], tlst[sr][sc] = tlst[sr][sc], [0,0]  # 상어를 먹이 위치로, 상어 자리는 빈 자리로
        shark_move(tlst, cnt + temp[0], movelst[i][0], movelst[i][1])           # 재귀
        tlst[movelst[i][0]][movelst[i][1]], tlst[sr][sc] = temp, tlst[movelst[i][0]][movelst[i][1]] # 상어 이동 전 먹이생선 부활, 상어 원위치
        tlst[sr][sc][1] = temp_shark_dir    # 상어 방향 원위치


lst = [[0]*4 for _ in range(4)]
for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(4):
        lst[i][j] = [temp[2*j], temp[2*j+1]-1]
res = 0
tempcnt = lst[0][0][0]
lst[0][0] = [-1,lst[0][0][1]]
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]


shark_move(lst,tempcnt,0,0)


print(res)
