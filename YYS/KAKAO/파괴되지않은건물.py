# def solution(board, skill):
#     cnt = 0
#     R = len(board)
#     C = len(board[0])
#     res = [[0 for _ in range(C)] for __ in range(R)]
#     for s in skill:
#         # s[0]이 1이면 공격
#         T = 1 if s[0] == 2 else -1
#         V = s[5] * T
#
#         # 왼쪽 위
#
#     for i in board:
#         for j in i:
#             if j > 0:
#                 cnt += 1
#
#     return cnt



# 누적합: 4 점을 잡고 각 행 먼저 계산 후 각 열 계산
def solution(board, skill):
    cnt = 0
    R = len(board)
    C = len(board[0])
    res = [[0 for _ in range(C+1)] for __ in range(R+1)]

    for s in skill:
        # s[0]이 1이면 공격
        T = 1 if s[0] == 2 else -1
        V = s[5] * T

        # 왼쪽 위
        res[s[1]][s[2]] += V
        # 오른쪽 위
        res[s[1]][s[4]+1] -= V
        # 왼쪽 아래
        res[s[3]+1][s[2]] -= V
        # 오른쪽 아래
        res[s[3]+1][s[4]+1] += V
    for r in range(R):
        for c in range(1, C):
            res[r][c] += res[r][c-1]
    for c in range(C):
        for r in range(1, R):
            res[r][c] += res[r-1][c]

    for i in range(R):
        for j in range(C):
            if board[i][j] + res[i][j] > 0:
                cnt += 1
    return cnt

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))