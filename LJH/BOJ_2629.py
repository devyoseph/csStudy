'''
BOJ
양팔저울
골드 3

https://www.acmicpc.net/problem/2629
'''


n = int(input())
chulst = list(map(int, input().split()))
balln = int(input())
balllst = list(map(int, input().split()))
dp = [[0]*15001 for _ in range(n+1)]
res = set()

def dfs(n,s,left,right):
    global dp, res
    w = abs(left-right)
    res.add(w)
    if s==n:
        return
    if dp[s][w]==0:
        dfs(n,s+1,left+chulst[s], right)
        dfs(n,s+1,left, right+chulst[s])
        dfs(n,s+1,left, right)
        dp[s][w] = 1



dfs(n,0,0,0)

for k in balllst:
    if k in res:
        print('Y', end=' ')
    else:
        print('N', end=' ')