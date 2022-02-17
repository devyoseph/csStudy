def dfs(row, col, n):
    global N, lst, white, blue

    S = 0

    # 모두 같은 색인지 검사하는 부분
    for i in range(n):
        for j in range(n):
            S += lst[row+i][col+j]

    if S == 0:
        white += 1
    elif S == n * n:
        blue += 1
    else:
        dfs(row, col, n // 2)  # 1 번째
        dfs(row, col + n // 2, n // 2)  # 2 번째
        dfs(row + n // 2, col, n // 2)  # 3 번째
        dfs(row + n // 2, col + n // 2, n // 2)  # 4 번째


N = int(input())
white = blue = 0
lst = []

for i in range(N):
    lst.append(list(map(int, input().split())))

dfs(0, 0, N)

print(white)
print(blue)
