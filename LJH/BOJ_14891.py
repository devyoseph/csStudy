from collections import deque

def func(num):
    while num<K:
        sg, d = lst[num][0], lst[num][1]
        i=0
        rcheck = [0]*5      # 회전 시킬 방향
        rcheck[sg] = d
        while sg+1+i<=4:    # 오른쪽 체크
            if globals()[f'g{sg+i}'][2] == globals()[f'g{sg+i+1}'][6]:
                break
            else:
                rcheck[sg+i+1] = -d
                d = -d
                i+=1
        i=0
        d = rcheck[sg]
        while sg-1-i>=1:    # 왼쪽 체크
            if globals()[f'g{sg-i}'][6] == globals()[f'g{sg-i-1}'][2]:
                break
            else:
                rcheck[sg-i-1] = -d
                d = -d
                i+=1
        for j in range(1,5):    # 회전
            if rcheck[j] == 1:  # 시계방향
                temp = globals()[f'g{j}'].pop()
                globals()[f'g{j}'].appendleft(temp)
            elif rcheck[j] == -1:   # 반시계방향
                temp = globals()[f'g{j}'].popleft()
                globals()[f'g{j}'].append(temp)
        num += 1

g1 = deque()
g2 = deque()
g3 = deque()
g4 = deque()

for i in range(1,5):
    for k in input():
        globals()[f'g{i}'].append(k)    # globals() 처음 써봅니다
K = int(input())
lst = [list(map(int, input().split())) for _ in range(K)]

func(0)
res = int(g1[0])*1+int(g2[0])*2+int(g3[0])*4+int(g4[0])*8
print(res)

