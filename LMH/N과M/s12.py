'''
BOJ
N과 M(12)
실버 3
5분
https://www.acmicpc.net/problem/15666
'''
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
lst = []
def dfs(dep, s):
    if dep == M:
        print(*lst)
        return
    prev = -1
    for i in range(s,N):
        if prev != arr[i]:
            prev = arr[i]
            lst.append(arr[i])
            dfs(dep+1, i)
            lst.pop()
dfs(0,0)