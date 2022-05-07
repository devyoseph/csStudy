def solution(rows, columns, queries):
    num = 1
    matrix = [[0 for _ in range(columns)] for __ in range(rows)]
    res = []
    for r in range(rows):
        for c in range(columns):
            matrix[r][c] = num
            num += 1

    for q in queries:

        a, b = q[0] - 1, q[1] - 1
        c, d = q[2] - 1, q[3] - 1
        R = c - a + 1
        C = d - b + 1

        save = matrix[a][b]  # 왼쪽 위에꺼 빼서 저장
        MIN = save
        for i in range(a + 1, c + 1):
            matrix[i - 1][b] = matrix[i][b]
            MIN = min(MIN, matrix[i - 1][b])

        for i in range(b + 1, d + 1):
            matrix[c][i - 1] = matrix[c][i]
            MIN = min(MIN,  matrix[c][i - 1])

        for i in range(c, a, -1):
            matrix[i][d] = matrix[i - 1][d]
            MIN = min(MIN, matrix[i][d])

        for i in range(d, b, -1):
            matrix[a][i] = matrix[a][i - 1]
            MIN = min(MIN, matrix[a][i])

        matrix[a][b + 1] = save

        res.append(MIN)

    return res

print(solution(6,6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3,3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100,97, [[1,1,100,97]]))