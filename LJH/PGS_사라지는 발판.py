'''
PGS
사라지는 발판
lv 3

https://programmers.co.kr/learn/courses/30/lessons/92345
'''
def Amove(board, aloc, bloc, amove, bmove):
    r, c = aloc
    if board[r][c]==0:
        print(['B win', amove + bmove])
        perfectwin.append(amove + bmove)
        return
    tempboard = [f[:] for f in board]
    flag = False
    for delta in range(4):
        nr = r+dr[delta]
        nc = c+dc[delta]
        if 0<=nr<height and 0<=nc<width and board[nr][nc]==1:
            flag = True
            tempboard[r][c]=0
            Bmove(tempboard, [nr,nc], bloc, amove+1, bmove)
    if flag==False:
        print(['B', amove+bmove])
        win.append(amove+bmove)
        return



def Bmove(board, aloc, bloc, amove, bmove):
    r, c = bloc
    if board[r][c]==0:
        print(['A win', amove + bmove])
        perfectwin.append(amove+bmove)
        return
    tempboard = [f[:] for f in board]
    flag = False
    for delta in range(4):
        nr = r + dr[delta]
        nc = c + dc[delta]
        if 0 <= nr < height and 0 <= nc < width and board[nr][nc] == 1:
            flag = True
            tempboard[r][c] = 0
            Amove(tempboard, aloc, [nr, nc], amove, bmove+1)
    if flag==False:
        print(['A', amove+bmove])
        win.append(amove + bmove)
        return

def solution(board, aloc, bloc):
    global height, width, perfectwin, win
    height = len(board)
    width = len(board[0])
    Amove(board, aloc, bloc, 0, 0)
    answer = 0
    if perfectwin:
        answer = max(perfectwin)
    else:
        answer = min(win)

    return answer

height, width = 0,0
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
perfectwin = []
win = []
print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1,0], [1,2]))
# print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1,0], [1,2]))