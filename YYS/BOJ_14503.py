N, M = list(map(int, input().split()))
r, c, d = list(map(int, input().split()))

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

debug = ["북","동","남","서"]
# 정상 방향
dxn = [-1, 0, 1, 0]
dyn = [0, 1, 0, -1]

d2 = [3, 0, 1, 2]  # 다음에 탐색할 방향

cnt = 0  # 청소한 구역 개수

flag = True  # 벽에 부딫히면 False로 변하는 Flag 변수

idx = 0
while flag:
    # idx += 1
    # print(idx,"번째 시도")
    if arr[r][c] == 0:  # 0인 경우
        arr[r][c] = 2  # 청소 완료는 2로 표기
        cnt += 1
        # print(r,c,"청소완료", debug[d])

    move = False # 주변에 청소할 곳이 없다고 가정하는 변수

    for i in range(4):
        d = d2[d] # 회전
        row = r + dxn[d]
        col = c + dyn[d]

        if row >= N or row < 0 or col < 0 or col >= M or arr[row][col] != 0:
            continue

        move = True
        r, c = row, col
        # print(r,c,"로 이동예정", debug[d])
        break

    # print(move)
    # break
    if move:
        continue
    # 만약 전방향 청소못한다면? 뒤로 움직일 수 있는지 확인, d는 늘 유지함
    else:
        r += dxn[(d + 2) % 4] # 방향 인덱스 2차이가 바라보는 반대방향
        c += dyn[(d + 2) % 4]

        if r < 0 or r >= N or c < 0 or c >= M or arr[r][c] == 1:
            flag = False


print(cnt)
