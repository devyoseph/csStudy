"""
BOJ
내리막 길
골드5
30분
https://www.acmicpc.net/problem/1520
"""
import sys
sys.setrecursionlimit(1000000)
def solve(i,j):
    # 목적지에 도착하면 1을 리턴
    if i == M-1 and j == N-1:
        return 1

    # 이미 방문한 적이 있다면, 그 위치에서 출발하는 경우의 수 리턴
    if dp[i][j] != -1:
        return dp[i][j]

    res = 0
    for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
        ni = i + di
        nj = j + dj
        if 0<= ni <M and 0<= nj <N and arr[i][j] > arr[ni][nj]:
            res += solve(ni,nj)

    dp[i][j] = res
    return dp[i][j]

M, N = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(M)]
dp = [[-1]*N for _ in range(M)]

print(solve(0,0))