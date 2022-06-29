"""
BOJ
팰린드롬?
골드4
1시간
https://www.acmicpc.net/problem/10942
"""
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
dp = [[0]*N for _ in range(N)]

for i in range(N-1):
    # 한글자 팰린드롬
    dp[i][i] = 1
    # 두글자 팰린드롬
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1
dp[N-1][N-1]=1

for nlen in range(2,N):
    for start in range(N-nlen):
        end = start + nlen
        # 가운데가 팰린드롬이면 팰린드롬
        if arr[start] == arr[end] and dp[start+1][end-1] == 1:
            dp[start][end] = 1

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S-1][E-1])