import copy
from pprint import pprint


def bfs(lst):
    dfslst = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if lst[r][c]>=5:
                cnt = 0
                for delta in range(4):
                    nr = r+dr[delta]
                    nc = c+dc[delta]
                    if 0<=nr<R and 0<=nc<C and not (nc == 0 and (nr == cleanc[0] or nr == cleanc[1])):
                        dfslst[nr][nc] += lst[r][c]//5
                        cnt += 1
                dfslst[r][c] -= cnt*(lst[r][c]//5)
    for r in range(R):
        for c in range(C):
            lst[r][c] += dfslst[r][c]

def clean(cu, cd):     # 청소한 부분이ㅣ 0이 나ㅗ오게 수정
    cr = cu
    cc = 0
    for delta in range(4):
        nr = cr
        nc = cc
        while 0<=nr<cu+1 and 0<=nc<C:
            if lst[nr][nc]>=0:
                lst[cr][cc] = lst[nr][nc]
            else:
                lst[cr][cc] = 0
            cr = nr
            cc = nc
            nr = cr + dr[delta]
            nc = cc + dc[delta]
    # lst[cu][0] = -1
    lst[cu][0] = 0
    lst[cu][1] = 0
    cr = cd
    cc = 0
    for delta in [2,1,0,3]:
        nr = cr
        nc = cc
        while cd <= nr < R and 0 <= nc < C:
            if lst[nr][nc] >= 0:
                lst[cr][cc] = lst[nr][nc]
            else:
                lst[cr][cc] = 0
            cr = nr
            cc = nc
            nr = cr + dr[delta]
            nc = cc + dc[delta]
    # lst[cd][0] = -1
    lst[cd][0] = 0
    lst[cd][1] = 0


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
R, C, T = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(R)]
cleanc = []
for i in range(R):
    if lst[i][0]== -1:
        cleanc.append(i)
i=0
cnt = 0
clst = copy.deepcopy(lst)
while i<T:
    cnt += 1
    bfs(lst)
    clean(cleanc[0], cleanc[1])
    if lst == clst:
        break
    clst = copy.deepcopy(lst)
    i+=1
    # if sum(lst[0])==0 and sum(lst[R])==0 and sum(lst[cleanc[0]]) and sum(lst[cleanc[1]])

result = 0
for i in range(R):
    result += sum(lst[i])
pprint(lst)
print(result, cnt)