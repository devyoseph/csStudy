'''
BOJ
N과 M(5)
실버 3
10분
https://www.acmicpc.net/problem/15654
'''

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
v = [0]*N

lst = []
def dfs(dep):
    if dep == M:
        print(*lst)
        return
    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            lst.append(arr[i])
            dfs(dep+1)
            v[i] = 0
            lst.pop()

dfs(0)