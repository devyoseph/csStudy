'''
BOJ
N과 M(6)
실버 3
5분
https://www.acmicpc.net/problem/15655
'''
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
v = [0]*N

ans = []
def dfs(dep,s):
    if dep == M:
        print(*ans)
        return
    for i in range(s,N):
        if v[i] == 0:
            v[i] = 1
            ans.append(arr[i])
            dfs(dep+1, i+1)
            v[i] = 0
            ans.pop()

dfs(0,0)