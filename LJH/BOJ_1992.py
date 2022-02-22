

def check(r, c, N):
    num = lst[r][c]
    for i in range(r,r+N):
        for j in range(c, c+N):
            if lst[i][j] != num:
                print('(',end='')
                check(r, c, N//2)
                check(r, c+N//2, N//2)
                check(r+N//2, c, N//2)
                check(r+N//2, c+N//2, N//2)
                print(')', end='')
                return
    if num:
        print('1', end='')
    else:
        print('0', end='')

N = int(input())
lst = [list(map(int, input())) for _ in range(N)]
check(0, 0, N)


