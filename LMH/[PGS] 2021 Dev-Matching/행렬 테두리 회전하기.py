"""
PGS
행렬 테두리 회전하기
level2
1시간
https://programmers.co.kr/learn/courses/30/lessons/77485
"""

def solution(rows, columns, queries):
    answer = []

    arr = [[0] * columns for _ in range(rows)]
    cnt = 1
    for r in range(rows):
        for c in range(columns):
            arr[r][c] = cnt
            cnt += 1

    for x1, y1, x2, y2 in queries:
        #  테두리 리스트 구하기
        tmp_arr = []
        tmp_arr += arr[x1 - 1][y1 - 1:y2]
        for r in range(x1, x2 - 1):
            tmp_arr.append(arr[r][y2 - 1])
        tmp_arr += arr[x2 - 1][y2 - 1:y1 - 1:-1]
        for r in range(x2 - 1, x1 - 1, -1):
            tmp_arr.append(arr[r][y1 - 1])

        answer.append(min(tmp_arr))

        # 시계방향 회전
        last = tmp_arr.pop()
        tmp_arr = [last] + tmp_arr

        # 테두리에 다시 값 집어넣기
        idx = 0
        for c in range(y1 - 1, y2):
            arr[x1 - 1][c] = tmp_arr[idx]
            idx += 1
        for r in range(x1, x2 - 1):
            arr[r][y2 - 1] = tmp_arr[idx]
            idx += 1
        for c in range(y2 - 1, y1 - 1, -1):
            arr[x2-1][c] = tmp_arr[idx]
            idx += 1
        for r in range(x2-1,x1-1,-1):
            arr[r][y1-1] = tmp_arr[idx]
            idx += 1

    return answer

ans = solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])
print(ans)