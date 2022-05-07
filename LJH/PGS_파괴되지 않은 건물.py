def solution(board, skill):
    # for action in skill:
    #     for r in range(action[1], action[3]+1):
    #         for c in range(action[2], action[4]+1):
    #             if action[0]==1:
    #                 board[r][c] -= action[5]
    #             else:
    #                 board[r][c] += action[5]
    #
    # answer = 0
    # for i in board:
    #     for j in i:
    #         if j>0:
    #             answer += 1
    answer = 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            for ac in skill:
                if ac[1]<=r<=ac[3] and ac[2]<=c<=ac[4]:
                    if ac[0]==1:
                        board[r][c] -= ac[5]
                    else:
                        board[r][c] += ac[5]
            if board[r][c]>0:
                answer += 1
    return answer



print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))