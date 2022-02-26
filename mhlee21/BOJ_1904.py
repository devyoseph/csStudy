"""
BOJ
01타일
실버3
30분
https://www.acmicpc.net/problem/1904
"""
# 방법 1 : 런타임 에러 (RecursionError)
# def dp(N): # N : 수열의 최대 길이
#     if N == 1:
#         return 1
#     elif N == 2:
#         return 2
#     elif N == 3:
#         return 3
#     else:
#         return dp(N-2) + dp(N-1)
#
# N = int(input())
# print(dp(N)%15746)

# 방법 2 :
# memoization, 재귀 없이 풀기
# stack 원소에 저장되는 값이 매우 클 수 있기 때문에 (메모리 초과) 저장하기 전 % 15746 해주어야 함
N = int(input())
stack = [0] * 1000001
stack[1] = 1
stack[2] = 2
stack[3] = 3
for i in range(4, N+1):
    stack[i] = (stack[i-2] + stack[i-1]) % 15746
print(stack[N])