# 지나갈 수 있는 길의 개수: NxN일 때 2N
# 경사로의 개수: 무한개
# 경사로를 놓는 칸의 높이는 경사로의 밑변만큼 모두 같아야한다
# 조건: 최소 경사로 밑변의 2배 길이만큼 공간이 확보되어야하고 사이의 차이가 1이넘는 경우 경사로가 불가능하다.

# 첫째줄 N, L: 길이

N, L = list(map(int, input().split()))
arr = []
cnt = 0  # 개수를 세어줄 변수


# 그냥 중간중간 이동할 수 있느냐 없느냐만 판단해주면 된다.
def check(lst):
    global N, L, arr, cnt

    visit = [False] * N
    prev = lst[0]
    now = lst[0]
    for idx in range(1, N):
        prev, now = now, lst[idx]  # 현재 높이
        d = now - prev
        if abs(d) > 1:
            return
        elif d == 1:  # 높이가 1 높아지는 경우: 이전에 경사로 설치
            if idx-L<0 or visit[idx-L]:
                return
            else:
                for i in range(idx-L,idx):
                    if lst[i] != now-1 or visit[i]:
                        return
                    visit[i] = True
        elif d == -1: # 높이가 1 낮아지는 경우
            if idx+L-1>=N:
                return
            else:
                for i in range(idx, idx+L):
                    if lst[i] != now or visit[i]:
                        return
                    visit[i] = True
    cnt += 1
    return


for i in range(N):
    arr.append(list(map(int, input().split())))
    check(arr[i])

for j in range(N):
    lst = []
    for i in range(N):
        lst.append(arr[i][j])
    check(lst)

print(cnt)
