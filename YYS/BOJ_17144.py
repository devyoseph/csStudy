# 10시 43분
import copy

R, C, T = tuple(map(int,input().split()))
lst = []

machine = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for r in range(R):
    lst.append(list(map(int,input().split())))
    
for c in range(R): # 여기서 R을 C로 써서 시간 증발
    if lst[c][0] == -1:
        machine = c
        break
#print(machine)
def spread(map):
    map2 = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            origin = map[i][j]
            if map[i][j] > 4:
                sp = origin//5
                for k in range(4):
                    row = i + dx[k]
                    col = j + dy[k]
                    if row<0 or row>=R or col<0 or col>=C or (row==machine and col==0) or (row==machine+1 and col==0):
                        continue
                    map2[row][col] += sp
                    origin -= sp
            map2[i][j] += origin
    # print("--------------")
    # for i in map2:
    #     print(i)
    # print("--------------")
    return map2

def wind(map):
    # 왼쪽 세로 위 >> 아래 바람
    for i in range(machine,0,-1):
        map[i][0] = map[i-1][0]
    # 왼쪽 세로 아래 >> 위 바람
    for i in range(machine+1,R-1):
        map[i][0] = map[i+1][0]

    map[machine][0] = map[machine+1][0] = 0

    # 맨 위 꼭대기 바람 오 >> 왼
    for j in range(0, C-1):
        map[0][j] = map[0][j+1]
    # 맨 아래 바람 오 >> 왼
    for j in range(0,C-1):
        map[R-1][j] = map[R-1][j+1]
    # 맨 오른쪽 아래 >> 위 바람
    for i in range(0,machine):
        map[i][C-1] = map[i+1][C-1]
    # 맨 오른쪽 위 >> 아래 바람
    for i in range(R-1,machine+1,-1):
        map[i][C-1] = map[i-1][C-1]
    # 기계에서 나가는 바람들
    for j in range(C-1,1,-1):
        map[machine][j] = map[machine][j-1]
        map[machine+1][j] = map[machine+1][j - 1]
    map[machine][1] = map[machine + 1][1] = 0
    # for i in map:
    #     print(i)
    return map

for t in range(T):
    lst = spread(lst)
    wind(lst)


S = 0
for i in lst:
    S += sum(i)
print(S)