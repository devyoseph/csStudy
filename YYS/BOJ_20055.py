N, K = list(map(int, input().split()))
q = list(map(int, input().split()))
robot = [0] * N  # 로봇을 저장할 리스트
level = 1

while True:
    q.insert(0,q.pop())
    robot.insert(0,robot.pop())
    robot[-1] = 0
    for i in range(N-2, 0, -1): # 로봇의 이동
        if robot[i] == 1 and robot[i+1] == 0 and q[i+1] > 0:
            robot[i+1] = 1
            robot[i] = 0
            q[i+1] -= 1
    robot[-1] = 0
    if q[0] > 0:
        q[0] -= 1
        robot[0] = 1

    if q.count(0) >= K:
        break
    level += 1
print(level)