def dfs(depth, start):
    global N, M, lst, visit

    if depth == M:
        print(*lst)
        return

    for i in range(start,N+1):
        if not visit[i]:
            visit[i] = True
            lst[depth] = i
            dfs(depth + 1,i+1)
            visit[i] = False


N, M = list(map(int, input().split()))

lst = [0] * M;  # 중간 값을 기록할 리스트
visit = [False] * (N+1)  # 방문 체크 배열

dfs(0,1);