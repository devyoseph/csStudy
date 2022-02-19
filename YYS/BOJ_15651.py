def dfs(depth):
    global N, M, lst

    if depth == M:
        print(*lst)
        return

    for i in range(1,N+1):

        lst[depth] = i
        dfs(depth + 1)



N, M = list(map(int, input().split()))

lst = [0] * M;  # 중간 값을 기록할 리스트

dfs(0);