'''
BOJ
N과 M(9)
실버 3
30분
https://www.acmicpc.net/problem/15663
'''
N,M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
v = [0]*N
lst = []
def dfs(dep):
    if dep == M:
        print(*lst)
        return
    prev = -1
    for i in range(N):
        if v[i] == 0 and prev != arr[i]:
            prev = arr[i]
            v[i] = 1
            lst.append(arr[i])
            dfs(dep+1)
            v[i] = 0
            lst.pop()
dfs(0)