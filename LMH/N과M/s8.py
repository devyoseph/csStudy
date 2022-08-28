'''
BOJ
N과 M(8)
실버 3
5분
https://www.acmicpc.net/problem/15657
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
        if not ans or ans[-1] <= arr[i]:
            ans.append(arr[i])
            dfs(dep+1)
            ans.pop()

dfs(0)