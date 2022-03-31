N = int(input())
lst = []
S = 0
MIN = 40000
for a in range(N):
    lst.append(list(map(int,input().split())))
    S += sum(lst[a])

def calcArea(x, y, d1, d2):
    global lst,S
    area = [0,0,0,0,0]
    # area1
    idx0 = 0
    for i in range(x):
        for j in range(y+1):
            area[1] += lst[i][j]
    for i in range(x, x+d1):
        for j in range(y-idx0):
            area[1] += lst[i][j]
        idx0+=1
    #area2
    idx3 = 1
    for i in range(x+d2+1):
        for j in range(y+d2+1, N):
            area[2] += lst[i][j]
    for j in range(y+1, y+d2+1):
        for i in range(x+idx3):
            area[2] += lst[i][j]
        idx3 += 1

    # # area3
    for i in range(x + d1, N):
        for j in range(y - d1):
            area[3] += lst[i][j]
    idx2 = 1
    for j in range(y - d1, y - d1 + d2):
        for i in range(x + d1 + idx2, N):
            area[3] += lst[i][j]
        idx2 += 1

    # #area4
    idx4 = 0
    for i in range(x+d1+d2+1,N):
        for j in range(y-d1+d2, N):
            area[4] += lst[i][j]
    for i in range(x+d2+1, x+d1+d2+1):
        for j in range(y+d2-idx4,N):
            area[4] += lst[i][j]
        idx4+=1

    #area5
    area[0] = S - sum(area)
    # print(" -----",x,y,d1,d2)
    # print(area[1], area[2],area[3], area[4], area[0])
    # print("최대", max(area),"최소", min(area))
    return max(area)-min(area)


for i in range(N): # i 가 행
    for j in range(N): # j 가 열
        for d1 in range(1, j):
            if i+d1 >= N:
                continue
            for d2 in range(1, N-j):
                if i+d1+d2 >= N:
                    continue
                MIN = min(calcArea(i,j,d1,d2),MIN)

print(MIN)
