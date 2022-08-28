"""
BOJ
경사로
골드3
1시간 20분
https://www.acmicpc.net/problem/14890
"""
def check(road):
    go = True
    visited = [True] * len(road) # 경사로를 놓았는지 기록할 배열
    for i in range(1, len(road)):
        diff = abs(road[i-1] - road[i])
        if diff > 1: # 높이 차이가 1이 아닌 경우
            go = False
            break
        elif diff == 1: # 높이 차이가 1인 경우
            if road[i-1] < road[i]: # 오르막일때
                cnt = 0
                for j in range(i-L,i):
                    if j >= 0 and road[j] == road[i-1] and visited[j]:
                        visited[j] = False
                        cnt += 1
                if cnt == L:
                    continue
            elif road[i-1] > road[i]: # 내리막일 때
                cnt = 0
                for j in range(i, i+L):
                    if j < N and road[j] == road[i] and visited[j]:
                        visited[j] = False
                        cnt += 1
                if cnt == L:
                    continue
            # if~elif 를 통해 continue 로 통과되지 않는 경우
            go = False
            break
    return go

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
res = 0

# 지나갈 수 있는 길인지 한 줄씩 검색 (가로)
for i in range(N):
    if check(arr[i]):
        # print(arr[i])
        res += 1

# 전치행렬을 통해 다시 검색 (세로)
arr_trans = list(map(list,zip(*arr)))
for i in range(N):
    if check(arr_trans[i]):
        # print('-',arr_trans[i])
        res += 1

print(res)