def dfs(depth):
    global cnt
    if depth == N:
        cnt += 1
        return

    for i in range(N):  # 깊이가 0일 때는 어디든 가능
        if depth == 0 or (not visited[i] and isPossible(depth, i)):
            visited[i] = True
            answer[depth] = i
            dfs(depth + 1)
            visited[i] = False


def isPossible(depth, col):
    judge = True
    for i in range(depth):
        if abs(depth - i) == abs(answer[i] - col):
            judge = False
            break
    return judge

N = int(input())
cnt = 0 # n-Queen의 개수
answer = [0 for i in range(N)] # N 크기의 배열 준비
visited = [False for i in range(N)] # 방문 체크 배열

dfs(0)

print(cnt)