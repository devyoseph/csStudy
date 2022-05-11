from pprint import pprint


def solution(board, aloc, bloc):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]


    R = len(board)
    C = len(board[0])

    Ax = aloc[0]
    Ay = aloc[1]

    Bx = bloc[0]
    By = bloc[1]

    # 백트래킹?

    def dfs(depth, WHO, Ax, Ay, Bx, By, board):
        #print(depth, WHO, Ax, Ay, Bx, By, board)
        if WHO == 'A':
            A_RESULT = list() # 결과들을 모아둔다.
            A_CAN_WIN = False # A가 이길 수 있는 경우라면 무조건 택해야 한다.
            A_CAN_MIN = 1000000
            if board[Ax][Ay] == 0:
                # print("====result====")
                # print(['B', depth])
                # print(depth, WHO, Ax, Ay, Bx, By)
                # pprint(board)
                return ['B', depth] # 승리자와 현재까지의 턴 수 리턴
            for k in range(4):
                row = Ax + dx[k]
                col = Ay + dy[k]

                if row < 0 or row >= R or col < 0 or col >= C:
                    continue
                if board[row][col] == 0:
                    continue

                board[Ax][Ay] = 0 # 움직일 수 있으므로 현재 발판 0으로 만들고
                A_RESULT.append(dfs(depth+1, 'B', row, col, Bx, By, board))
                if A_RESULT[-1][0] == 'A':
                    A_CAN_WIN = True
                    A_CAN_MIN = min(A_CAN_MIN, A_RESULT[-1][1]) # A가 이기는 경우 depth의 최소값 갱신
                board[Ax][Ay] = 1 # 백트래킹을 위해 발판을 되돌림

            if len(A_RESULT) == 0:
                return ['B', depth] # 만약 움직일 수 없어도 B의 승리
            elif A_CAN_WIN:
                for r in A_RESULT:
                    if r[1] == A_CAN_MIN:
                        return r
            else: # A가 이기는 경우가 없다면 질질 끌어야 한다.
                B_MAX = 0
                B_RES = [[]]
                for r in A_RESULT:
                    if r[1] > B_MAX:
                        B_RES[0] = r
                return B_RES[0]

        elif WHO == 'B':
            B_RESULT = list()  # 결과들을 모아둔다.
            B_CAN_WIN = False  # B가 이길 수 있는 경우라면 무조건 택해야 한다.
            B_CAN_MIN = 1000000
            if board[Bx][By] == 0:
                # print("====result====")
                # print(['A', depth])
                # print(depth, WHO, Ax, Ay, Bx, By)
                # pprint(board)
                return ['A', depth]  # 승리자와 현재까지의 턴 수 리턴
            #possible = False
            for k in range(4):
                row = Bx + dx[k]
                col = By + dy[k]

                if row < 0 or row >= R or col < 0 or col >= C:
                    continue
                if board[row][col] == 0:
                    continue

                board[Bx][By] = 0  # 움직일 수 있으므로 현재 발판 0으로 만들고
                B_RESULT.append(dfs(depth + 1, 'A', Ax, Ay, row, col, board))
                if B_RESULT[-1][0] == 'B':
                    B_CAN_WIN = True
                    B_CAN_MIN = min(B_CAN_MIN, B_RESULT[-1][1])  # A가 이기는 경우 depth의 최소값 갱신
                board[Bx][By] = 1  # 백트래킹을 위해 발판을 되돌림

            if len(B_RESULT) == 0:
                return ['A', depth]  # 만약 움직일 수 없어도 B의 승리
            elif B_CAN_WIN:
                for r in B_RESULT:
                    if r[1] == B_CAN_MIN:
                        return r
            else: #B가 이기는 경우가 없다면 A가 이긴다해도 질질 끈다
                A_MAX = 0
                A_RES = [[]]
                for r in B_RESULT:
                    if r[1] > A_MAX:
                        A_RES[0] = r

                return A_RES[0]



    return dfs(0, 'A', Ax, Ay, Bx, By, board)[1]
