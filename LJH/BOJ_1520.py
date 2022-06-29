'''
BOJ
내리막 길
골드 4

https://www.acmicpc.net/problem/1520
'''
import sys
input = sys.stdin.readline

def dfs(r,c):
    global dp
    if r==m-1 and c==n-1:
        return 1
    if dp[r][c]!=-1:
        return dp[r][c]
    temp = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<m and 0<=nc<n and lst[r][c] > lst[nr][nc]:
            temp += dfs(nr,nc)
    dp[r][c] = temp
    return dp[r][c]

m, n = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1 for _ in range(n)] for _ in range(m)]
dr = [0,0,1,-1]
dc = [1,-1,0,0]
# dp[0][0] = 1
dfs(0,0)
print(dp[0][0])