'''
BOJ
N과 M(7)
실버 3
5분
https://www.acmicpc.net/problem/15656
'''
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []
def dfs(dep):
    if dep == M:
        print(*ans)
        return
    for i in range(N):
        ans.append(arr[i])
        dfs(dep+1)
        ans.pop()
dfs(0)