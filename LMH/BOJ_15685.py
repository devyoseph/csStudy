"""
BOJ
드래곤커브
골드4
1시간
https://www.acmicpc.net/problem/15685
"""
# x축 : 가로(C), y축 : 세로(R)
# 0: x좌표가 증가하는 방향 (→)
# 1: y좌표가 감소하는 방향 (↑)
# 2: x좌표가 감소하는 방향 (←)
# 3: y좌표가 증가하는 방향 (↓)
dist = [(0,1),(-1,0),(0,-1),(1,0)] # 주어진 방향 : 0, 1, 2, 3
arr = [[0]*101 for _ in range(101)]

def makedist(g):
    if g == 0:
        return
    idx = len(stack) - 1
    while idx >= 0:
        dist = stack[idx]
        stack.append((dist+1)%4)
        idx -= 1
    makedist(g-1)

def setpoints(x, y, stack):
    # print('[',x,y,']')
    arr[y][x] = 1
    idx = 0
    r, c = y, x
    while idx < len(stack):
        dr, dc = dist[stack[idx]]
        idx += 1
        r += dr
        c += dc
        if 0<= r <= 100 and 0<= c <= 100 and arr[r][c] == 0:
            # print(r,c)
            arr[r][c] = 1

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
for x,y,d,g in lst:
    stack = [d]
    makedist(g)
    setpoints(x, y, stack)

res = 0
for i in range(101-1):
    for j in range(101-1):
        if arr[i][j] and arr[i][j+1] and arr[i+1][j] and arr[i+1][j+1]:
            # print('(',i,j,')')
            res += 1
print(res)