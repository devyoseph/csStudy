def solution(maps):
    global N, M, visit, nation, dx, dy, max_nation, visit2, MAPS
    N = len(maps)
    M = len(maps[0])

    dx = [0,0,1,-1]
    dy = [-1,1,0,0]
    visit = [[False for _ in range(M)] for __ in range(N)]
    visit2 = [[False for _ in range(M)] for __ in range(N)]
    MAPS = [["" for _ in range(M)] for __ in range(N)]
    #print(N,M)
    for n in range(N):
        for m in range(M):
            #print(n, m)
            #print(maps[n][m])

            MAPS[n][m] = maps[n][m]

    nation = []
    max_nation = 0
    def dfs(R, C):
        global N, M, visit, nation, dx, dy, MAPS

        visit[R][C] = True
        if maps[R][C] != ".":
            nation[ord(maps[R][C])-65] += 1

        for k in range(4):
            row = R + dx[k]
            col = C + dy[k]

            if row <0 or row >= N or col <0 or col >=M:
                continue
            elif visit[row][col] or maps[row][col] == ".":
                continue


            dfs(row, col)

    def dfs2(R, C, hubo, max_nation):
        global N, M, visit2, dx, dy, MAPS

        visit2[R][C] = True
        if MAPS[R][C] in hubo:
            MAPS[R][C] = max_nation
        for k in range(4):
            row = R + dx[k]
            col = C + dy[k]

            if row <0 or row >= N or col <0 or col >=M:
                continue
            elif visit2[row][col] or maps[row][col] == ".":
                continue


            dfs2(row, col, hubo, max_nation)


    for n in range(N):
        for m in range(M):
            if not visit[n][m] and maps[n][m] != ".":
                nation = [0]*26
                dfs(n,m)
                max_nation = 0
                MAX = 0
                for na in range(len(nation)):
                    if MAX <= nation[na]:
                        max_nation = na
                        MAX = nation[na]
                hubo = []
                for na in range(len(nation)):
                    if nation[na] != 0 and MAX > nation[na]:
                        hubo.append(chr(na+65))
                dfs2(n,m, hubo, chr(max_nation+65))
                #print(nation, n, m)

    nation = [0]*26
    for n in range(N):
        for m in range(M):
            if MAPS[n][m] != ".":
                nation[ord(MAPS[n][m])-65] += 1
    return max(nation)

print(solution(["AABCA.QA", "AABC..QX", "BBBC.Y..", ".A...T.A", "....EE..",".M.XXEXQ","KL.TBBBQ"]))
#print(solution(["XY..", "YX..", "..YX", ".AXY"]))