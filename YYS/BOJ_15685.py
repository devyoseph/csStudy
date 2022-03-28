N = int(input())

rotate = [1, 2, 3, 0]  # 회전시 결과 방향
move = [[1, 0], [0, -1], [-1, 0], [0, 1]]
dragon = []  # 회전 방향에 따라 어떻게 될지 모르므로 일단 모두 기록한다

area = [[False] * 101 for i in range(101)]

for i in range(N):
    x, y, d, g = list(map(int, input().split()))
    dragon.append(list())
    dragon[-1].append(d)
    # print(dragon)
    area[x][y] = True  # 시작점 포함
    x += move[d][0]
    y += move[d][1]

    if 0 <= x <= 100 and 0 <= y <= 100:
        area[x][y] = True

    for j in range(g):
        L = len(dragon[i])
        for idx in range(L - 1, -1, -1):
            dragon[i].append(rotate[dragon[i][idx]])
            x += move[dragon[i][-1]][0]
            y += move[dragon[i][-1]][1]
            if 0 <= x <= 100 and 0 <= y <= 100:
                area[x][y] = True
        # print(dragon[i])
# print(dragon)
cnt = 0
for i in range(100):
    for j in range(100):
        if True == area[i][j] == area[i][j + 1] == area[i + 1][j] == area[i + 1][j + 1]:
            cnt += 1

print(cnt)
