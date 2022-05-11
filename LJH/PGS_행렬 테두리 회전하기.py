'''
PGS
행렬 테두리 회전하기
lv 2
40분
https://programmers.co.kr/learn/courses/30/lessons/77485
'''
from pprint import pprint


def roll(r1,c1,r2,c2):
    r1,r2,c1,c2 = r1-1,r2-1,c1-1,c2-1
    global lst
    nr,nc = r1,c1
    temp = lst[nr][nc]
    slst = [temp]
    for delta in range(4):
        while r1<=nr+dr[delta]<=r2 and c1<=nc+dc[delta]<=c2:
            nr += dr[delta]
            nc += dc[delta]
            lst[nr][nc], temp = temp, lst[nr][nc]
            slst.append(temp)
    return min(slst)



def solution(rows, columns, queries):
    global lst
    lst = [list([0]*columns) for _ in range(rows)]
    temp = 1
    answer = []
    for r in range(rows):
        for c in range(columns):
            lst[r][c] = temp
            temp+=1
    for querie in queries:
        a = roll(*querie)
        answer.append(a)

    return answer

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))