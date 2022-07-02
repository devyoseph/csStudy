from collections import deque


def solution(board, r, c):
    # dfs 를 두개? : 하나는 현재 점에서 최소가 되는 그림찾기 / 전체를 고려한 DFS
    MAX = 0
    for item in board:
        for i in item:
            MAX = max(i, MAX)  # 일단 최대 번호 찾기

    visit = [False] * (MAX + 1)
    mapping = [[-1, -1, -1, -1] for _ in range(MAX + 1)]
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                now = board[i][j]
                if mapping[now][0] == -1:  # 처음 기록된 것이라면
                    mapping[now][0] = i
                    mapping[now][1] = j
                else:
                    mapping[now][2] = i
                    mapping[now][3] = j

    global ans
    ans = float("inf")

    # 살짝 브루트포스틱하게
    def bfs_Path(r1, c1, r2, c2, board):  # (r1, c1)에서 (r2, c2)로 이동할 수 있는 최소 버튼
        #print("bfs")
        if r1 == r2 and c1 == c2:
            return 0

        global ans, min_Path
        # BFS로 변경
        visit = [[float("inf")] * 4 for _ in range(4)]  # 방문체크
        q = deque()
        q.appendleft([r1, c1, 0])  # 시작점 넣어주기
        visit[r1][c1] = 0

        while q:
            now = q.pop()
            r = now[0]
            c = now[1]
            input = now[2]
            #print("현재 점의 위치:", r, c, input)
            if (r == r2 and c == c2) or visit[r][c] < input:
                #print("도착 점의 위치:", r, c, input)
                #print(q)
                continue

            for k in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                row = r + k[0]
                col = c + k[1]

                if row < 0 or row >= 4 or col < 0 or col >= 4:
                    continue

                if visit[row][col] > input + 1:
                    visit[row][col] = input + 1
                    q.appendleft([row, col, input + 1])
                # 한 번 이동한 것에 만약 다른 카드가 있었다면 ctrl을 굳이 적용할 필요가 없다

                # 한칸 움직였는데 카드가 있는 곳이었다면 굳이 ctrl을 쓸 필요가 없다
                if board[row][col] != 0:
                    continue

                while 0 <= row < 4 and 0 <= col < 4 and board[row][col] == 0:
                    row += k[0]
                    col += k[1]

                # print("멈춤:",row,col)
                # 여기 내려온 값은 최소 한 번은 이동함: 그 이후 경계값을 벗어나거나 카드를 만난 것
                if row < 0 or row >= 4 or col < 0 or col >= 4:  # 만약 경계값을 벗어났으면
                    if visit[row - k[0]][col - k[1]] > input + 1:
                        visit[row - k[0]][col - k[1]] = input + 1
                        q.appendleft([row - k[0], col - k[1], input + 1])

                elif board[row][col] != 0 and visit[row][col] > input + 1:
                    visit[row][col] = input + 1
                    q.appendleft([row, col, input + 1])

        return visit[r2][c2]

        # # 가지치기
        # if min_Path <= SUM or SUM > 6:
        #     return

        # # 도달
        # if r1 == r2 and c1 == c2:
        #     min_Path = min(min_Path, SUM)
        #     print("갱신 :", SUM)
        #     return
        # # 그냥 4방향으로 1씩 옮겨보기 / ctrl + 4방향으로 옮겨보기
        # for k in [[0,1], [0,-1], [1,0], [-1,0]]:
        #     row = r1 + k[0]
        #     col = c1 + k[1]

        #     if row<0 or row>=4 or col<0 or col>=4:
        #         continue
        #     dfs_Path(row,col, r2,c2, board, SUM+1)

        #     # 한 번 이동한 것에 만약 다른 카드가 있었다면 ctrl을 굳이 적용할 필요가 없다
        #     if board[row][col] != 0:
        #         continue

        #     # 만약 이동한 곳이 0이라면 ctrl을 적용할 수 있는지 확인
        #     while (row>=0 and row<4 and col>=0 and col<4) or board[row][col] == 0:
        #         row = r1 + k[0]
        #         col = c1 + k[1]

        #     # 여기 내려온 값은 최소 한 번은 이동함: 그 이후 경계값을 벗어나거나 카드를 만난 것
        #     if row<0 or row>=4 or col<0 or col>=4: # 만약 경계값을 벗어났으면
        #         dfs_Path(row-k[0],col-k[1], r2,c2, board, SUM+2) # 그 이전 값으로 되돌려주고 ctrl 적용(+2)

        #     elif board[row][col] == 0:
        #         dfs_Path(row,col,r2,c2,board,SUM+2)

    def dfs_Select(MAX, depth, r, c, visit, board, SUM_ALL, mapping):
        global ans
        # 가지치기
        #print(depth, visit, r, c, SUM_ALL)
        if ans <= SUM_ALL:
            return

        if depth == MAX:  # 모든 짝을 맞췄다면
            #print('최종결과:', SUM_ALL)
            ans = min(SUM_ALL, ans)
            return

        for index in range(1, MAX + 1):
            if not visit[index]:  # 방문안한 곳이라면
                visit[index] = True  # 방문 체크
                # print(visit)
                a = bfs_Path(r, c, mapping[index][0], mapping[index][1], board)
                b = bfs_Path(mapping[index][0], mapping[index][1], mapping[index][2], mapping[index][3], board)
                board[mapping[index][0]][mapping[index][1]] = 0
                board[mapping[index][2]][mapping[index][3]] = 0
                #print(r, c, " => ", mapping[index][0], mapping[index][1], " => ", mapping[index][2], mapping[index][3]," 선택 / 중간 결과:", a + b, a, b)
                dfs_Select(MAX, depth + 1, mapping[index][2], mapping[index][3], visit, board, SUM_ALL + a + b, mapping)

                board[mapping[index][0]][mapping[index][1]] = index
                board[mapping[index][2]][mapping[index][3]] = index
                a = bfs_Path(r, c, mapping[index][2], mapping[index][3], board)
                b = bfs_Path(mapping[index][2], mapping[index][3], mapping[index][0], mapping[index][1], board)

                board[mapping[index][0]][mapping[index][1]] = 0
                board[mapping[index][2]][mapping[index][3]] = 0
                #print(r, c, " => ", mapping[index][2], mapping[index][3], " => ", mapping[index][0], mapping[index][1]," 선택 / 중간 결과:", a + b, a, b)
                dfs_Select(MAX, depth + 1, mapping[index][0], mapping[index][1], visit, board, SUM_ALL + a + b, mapping)

                visit[index] = False  # 방문 해제
                board[mapping[index][0]][mapping[index][1]] = index
                board[mapping[index][2]][mapping[index][3]] = index

    dfs_Select(MAX, 0, r, c, visit, board, 0, mapping)
    return ans + MAX * 2


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1))
