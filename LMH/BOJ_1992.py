"""
BOJ
쿼드트리
실버1
15분
https://www.acmicpc.net/problem/1992
"""
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
result = []

def solve(r,c,N):
    check = arr[r][c]
    for i in range(r,r+N):
        for j in range(c,c+N):
            if check != arr[i][j]:
                result.append('(')
                solve(r,c,N//2)
                solve(r,c+N//2,N//2)
                solve(r+N//2,c,N//2)
                solve(r+N//2,c+N//2,N//2)
                result.append(')')
                return
    if check == 0:
        result.append('0')
    else:
        result.append('1')

solve(0,0,N)
print(''.join(result))