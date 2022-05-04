import sys
sys.stdin = open('sample_input.txt', 'r')

def solve(i, j, cnt, flag):
    global ans
    ans = max(ans, cnt)
    for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni, nj = i + di, j + dj
        if 0<=ni<N and 0<=nj<N and visited[ni][nj] == False:
            visited[ni][nj] = True
            if not flag and arr[ni][nj] >= arr[i][j] and (arr[ni][nj] - arr[i][j]) < K:
                tmp = arr[ni][nj]
                arr[ni][nj] = arr[i][j] - 1
                solve(ni, nj, cnt+1, True)
                arr[ni][nj] = tmp
            elif arr[ni][nj] < arr[i][j]:
                solve(ni, nj, cnt+1, flag)
            visited[ni][nj] = False


T = int(input())
for test_case in range(1,T+1):
    N, K = map(int, input().split())
    arr = []
    max_point = 0
    for i in range(N):
        arr.append(list(map(int, input().split())))
        max_point = max(max_point,*arr[i])

    ans = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_point:
                visited[i][j] = True
                solve(i, j, 1, False)
                visited[i][j] = False

    print(f'#{test_case} {ans}')