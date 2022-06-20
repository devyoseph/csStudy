import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(arr, visit, res, n):
    global number
    visit[n] = True
    res[n] = number
    number = number + 1
    for x in arr[n]:
        if not visit[x]:
            dfs(arr, visit, res, x)

N, M, R = map(int, input().split())
# arr = [[0 for _ in range(N)] for __ in range(N)]
arr = [list() for _ in range(N)]
res = [0]*N # 결과 저장
visit = [False]*N
number = 1

for _ in range(M):
    a, b = map(int, input().split())
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)

for a in arr:
    a.sort();

dfs(arr, visit, res, R-1)

for i in range(N):
    print(res[i])