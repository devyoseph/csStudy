"""
BOJ
RGB거리
실버1
45분
https://www.acmicpc.net/problem/1149
"""
## 방법 1. 시간초과
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# visited = [-1] * N
# min_total = 1000*N
#
# def check(varr):
#     # 주어진 배열이 다음 규칙을 만족하는지 검사
#     # i 번째 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.
#     for i in range(1,len(varr) -1):
#         if varr[i] == varr[i-1] or varr[i] == varr[i+1]:
#             return False
#     return True
#
# def solve(house, N):
#     global min_total
#     if house == N:
#         if check(visited): #배열이 규칙 만족하는 경우 비용 계산
#             total = 0
#             for i in range(N):
#                 total += arr[i][visited[i]]
#             min_total = min(min_total, total) # 최솟값 구하기
#         return
#     for color in range(3):
#         if visited[house] == -1:
#             visited[house] = color
#             solve(house+1, N)
#             visited[house] = -1
#
# solve(0,N)
# print(min_total)

# 방법 2 : 시간초과 (이게 아닌가보다..)
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# visited = [-1] * N
# color = [0,1,2] # 0:R, 1:G, 2:B
# min_total = 1000*N
#
# def solve(c,num,N):
#     global min_total
#     visited[num] = c
#     if num == N-1:
#         total = 0
#         for i in range(N):
#             total += arr[i][visited[i]]
#         min_total = min(min_total, total) # 최솟값 구하기
#         return
#     else:
#         solve((c+1)%3,num+1,N)
#         solve((c+2)%3,num+1,N)
#
# for i in color:
#     solve(i,0,N)
# print(min_total)

# 방법 3 : 누적 최소값을 이용 (wow...)
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(1,N):
    arr[i][0] += min(arr[i - 1][1], arr[i - 1][2])
    arr[i][1] += min(arr[i - 1][0], arr[i - 1][2])
    arr[i][2] += min(arr[i - 1][0], arr[i - 1][1])
print(min(arr[N-1]))