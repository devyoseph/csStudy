"""
BOJ
색종이 만들기
실버3
1시간
https://www.acmicpc.net/problem/2630
"""

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
blue = white = 0

def solve(r,c,N):
    global blue, white
    # print(r,c)
    check = arr[r][c]
    for i in range(r,r+N):
        for j in range(c,c+N):
            if check != arr[i][j]:
                solve(r,c,N//2)
                solve(r,c+N//2,N//2)
                solve(r+N//2,c,N//2)
                solve(r+N//2,c+N//2,N//2)
                return
    if check:
        blue += 1
    else:
        white += 1

solve(0,0,N)
print(white)
print(blue)
