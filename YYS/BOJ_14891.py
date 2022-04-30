# 톱니바퀴는 4개, 톱니는 8개

gear = []
top = [0, 0, 0, 0]  # 0번이 처음에는 기준이지만 7번까지 맨 꼭대기 변경 가능

for g in range(4):
    gear.append(input())

K = int(input())

def pole(n, direction):
    global gear, top
    number = 0
    if n < 0 or n > 3:
        return -1
    if direction == "left":
        number = 6
    elif direction == "right":
        number = 2

    return int(gear[n][(top[n] + number) % 8])


def dfs(n, d, visit):
    global gear, top
    if n < 0 or n > 3 or visit[n]:
        return
    visit[n] = True
    # print(n+1,"번",d,"방향회전")
    # 현재 n번째 양옆의 톱니바퀴와 방향 유무를 판단하기 위해 두 방향의 합은 1이어야 한다. (0과 1)
    if pole(n, "left") + pole(n - 1, "right") == 1:
        dfs(n - 1, d * (-1), visit)  # 다른 톱니바퀴의 회전 방향을 알려주고
    if pole(n, "right") + pole(n + 1, "left") == 1:
        dfs(n + 1, d * (-1), visit)

    top[n] = (top[n] - d) % 8


for k in range(K):
    n, d = list(map(int,input().split()))  # 톱니 번호, 회전: 1 시계, -1 반시계

    # 현재 n번째 톱니바퀴의 2번과 6번을 구하고 양 옆의 톱니바퀴가 그값과 같다면 회전한다.
    dfs(n-1, d, [False] * 4)
    # print(top)

S = 0
# print(gear)
for i in range(4):
    S += int(pow(2, i))*int(gear[i][top[i]])
print(S)
