
def sol():
    for i in range(N):
        x, y, d, g = lst[i]
        field[y][x] = 1
        dradir = [d]
        for j in range(g):
            for l in range(len(dradir)-1, -1, -1):
                dradir.append(oppose[dradir[l]])
        for k in dradir:
            y += dr[k]
            x += dc[k]
            field[y][x] = 1

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
oppose = [1,2,3,0]
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

field = [[0]*101 for _ in range(101)]
sol()
cnt = 0
for i in range(100):
    for j in range(100):
        if field[i][j] and field[i+1][j] and field[i][j+1] and field[i+1][j+1]:
            cnt += 1
print(cnt)
