from pprint import pprint

def bfs(map, RBO):
    q = []
    cnt = -1
    RX = RBO[0]
    RY = RBO[1]
    BX = RBO[2]
    BY = RBO[3]
    X0 = RBO[4]
    Y0 = RBO[5]

    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    q.insert(0,[RX,RY,BX,BY,0])


    while len(q) != 0:
        now = q.pop()
        S = now[4] # 지금까지 움직인 횟수
        #꺼내고 좌표가 -라면 공이 들어간 상태임: 만약 R이 - 면 무조건
        #스킵 B만 - 면 그게 답
        if S > 10:
            continue
        if now[2] < 0:
            continue
        elif now[1] < 0:
            cnt = S
            break


        for k in range(4):
    #먼저 기울일 때 벽에 도착하는 구슬을 움직여야한다.
            red = False # 빨강이 먼저인지 아닌지 결정
            if k == 0:  #위로 움직일 때
                red = True if now[0] < now[2] else False
            elif k == 1:  # 아래로 움직일 때
                red = False if now[0] < now[2] else True
            elif k == 2:  # 왼쪽으로 움직일 때
                red = True if now[1] < now[3] else False
            elif k == 3:  # 오른쪽으로 움직일 때
                red = False if now[1] < now[3] else True

            redX = now[0]
            redY = now[1]
            blueX = now[2]
            blueY = now[3]

            while red : # 빨강먼저면 카운트
                if map[redX+dx[k]][redY+dy[k]] == '#':
                    break
                elif redX + dx[k] == blueX and redY + dy[k] == blueY:
                    break
                redX += dx[k]
                redY += dy[k]

                if redX == X0 and redY == Y0 :
                    redX=-1
                    redY=-1
                    break

            while True:
                if map[blueX+dx[k]][blueY+dy[k]] == '#':
                    break
                elif blueX + dx[k] == redX and blueY + dy[k] == redY:
                    break

                blueX += dx[k]
                blueY += dy[k]

                if blueX == X0 and blueY == Y0:
                    blueX=-1
                    blueY=-1
                    break

            while not red:
                if map[redX+dx[k]][redY+dy[k]] == '#':
                    break
                elif redX + dx[k] == blueX and redY + dy[k] == blueY:
                    break

                redX += dx[k]
                redY += dy[k]
                
                if redX == X0 and redY == Y0:
                    redX=-1
                    redY=-1
                    break

            if redX == now[0] and redY == now[1] and blueX == now[2] and blueY == now[3]:
                 continue
            q.insert(0,[redX, redY, blueX, blueY, S + 1])
    print(cnt)

N, M = map(int, input().split())

map = [['.'for _ in range(M)] for __ in range(N)]
RBO = [0]*6
for i in range(N):
    now = input()
    for j in range(M):
        if now[j] == 'R':
            RBO[0] = i
            RBO[1] = j
        elif now[j] == 'B':
            RBO[2] = i
            RBO[3] =j
        elif now[j] == 'O':
            RBO[4] = i
            RBO[5] = j
        else:
            map[i][j] = now[j]
# pprint(map)

bfs(map, RBO)