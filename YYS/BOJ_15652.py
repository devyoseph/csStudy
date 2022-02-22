def dfs(depth,start):
    global N, M, lst

    if depth == M:
        print(*lst)
        return

    for i in range(start,N+1):

        lst[depth] = i
        dfs(depth + 1,i)



N, M = list(map(int, input().split()))

lst = [0] * M;  # 중간 값을 기록할 리스트

dfs(0,1);