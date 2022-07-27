'''
BOJ
N과 M(11)
실버 3
5분
https://www.acmicpc.net/problem/15665
'''
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
lst = []
def dfs(dep):
    if dep == M:
        print(*lst)
        return
    prev = -1
    for i in range(N):
        if prev != arr[i]:
            prev = arr[i]
            lst.append(arr[i])
            dfs(dep+1)
            lst.pop()
dfs(0)