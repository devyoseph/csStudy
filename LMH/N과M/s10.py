'''
BOJ
N과 M(10)
실버 3
5분
https://www.acmicpc.net/problem/15664
'''
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
v = [0] * N
lst = []
def dfs(dep, s):
    if dep == M:
        print(*lst)
        return
    prev = -1
    for i in range(s,N):
        if v[i] == 0 and prev != arr[i]:
            prev = arr[i]
            v[i] = 1
            lst.append(arr[i])
            dfs(dep+1, i+1)
            v[i] = 0
            lst.pop()

dfs(0,0)