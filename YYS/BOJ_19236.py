# 1 <= 번호 <= 16
# 방향 8방향
# 7시 45분
# 상어 : 0,0 출발
# 물고기 이동: 번호가 작은 물고기부터 이동: 빈칸 + 다른 물고기 모두 가능(대신 위치바꿈) + 상어칸 X
# 이동할 수 있는 곳을 찾을 때까지 반시계 회전
# 상어는 이동할 수 있는 칸이 없으면 집을 가며 이동할 수 있으면 여러 칸을 이동할 수 있다.
# 상어가 먹을 수 있는 번호합의 최대값

# 4x4 공간 고정이므로 DFS로 풀이한다.
import copy
from pprint import pprint

arr = [[[0, 0] for _ in range(4)] for __ in range(4)]
for i in range(4):
    lst = list(map(int, input().split()))
    for j in range(4):
        arr[i][j][0] = lst[j * 2]
        arr[i][j][1] = (lst[j * 2 + 1] - 1) % 8  # 그냥 1 빼고 나눔

# 방향 정리
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]  # 반시계 좌표

# 상어 관련 변수
MAX = 0

def fish(arr, x, y):
    global dx, dy
    q = []  # 먼저 리스트로 받기
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == 0:
                continue
            q.append(arr[i][j][0])  # 물고기 번호만 넣기
    q.sort()
    # print(q)

    for m in range(len(q)):
        find = False
        for r in range(4):
            if find: break
            for c in range(4):
                if arr[r][c][0] == q[m]:
                    score = arr[r][c][0]
                    direction = arr[r][c][1]

                    for k in range(8):  # 8방향 검사
                        row, col = r + dy[(direction + k) % 8], c + dx[(direction + k) % 8]
                        if row < 0 or row >= 4 or col < 0 or col >= 4 or (row == x and col == y):
                            continue  # 상어가 있거나 경계선을 벗어나면

                        if arr[row][col][0] > 0:
                            arr[row][col][0], arr[row][col][1], arr[r][c][0], arr[r][c][1] = score, (direction + k) % 8, \
                                                                                             arr[row][col][0], \
                                                                                             arr[row][col][1]

                        else:
                            arr[row][col][0], arr[row][col][1] = score, (direction + k) % 8
                            arr[r][c][0], arr[r][c][1] = 0, 0
                        break
                    find = True
                    break


def simulate(arr, x, y, sum):
    global dx, dy, MAX
    catch = False
    arr2 = copy.deepcopy(arr) # 방문 체크 형식X 그냥 deep copy
    d = arr2[x][y][1]
    sum += arr2[x][y][0]
    arr2[x][y][1] = arr2[x][y][0] = 0

    fish(arr2, x, y)
    #pprint(arr2)
    #print(sum)
    while True:
        x += dy[d]
        y += dx[d]
        #print(x, y)
        if x < 0 or x >= 4 or y < 0 or y >= 4:
            break

        if arr2[x][y][0] > 0:
            simulate(arr2, x, y, sum)
            catch = True

    if not catch:
        MAX = max(MAX, sum)


simulate(arr, 0, 0, 0)
print(MAX)
