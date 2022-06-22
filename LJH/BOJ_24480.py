'''
BOJ
알고리즘 수업 - 깊이 우선 탐색 2
실버 2
1분
https://www.acmicpc.net/problem/24480
'''
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N, M, R = map(int, input().split())
lst = [[] for _ in range(N+1)]
visited = [0]*(N+1)

def dfs(s):
    global cnt
    visited[s] = cnt
    cnt += 1
    for k in lst[s]:
        if visited[k]==0:
            dfs(k)


for _ in range(M):
    u,v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)

for i in range(1,N+1):
    lst[i].sort(reverse=True)

cnt = 1
dfs(R)

for i in visited[1:]:
    print(i)