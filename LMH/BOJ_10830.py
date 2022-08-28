"""
BOJ
행렬 제곱
골드4
1시간
https://www.acmicpc.net/problem/10830
"""

# # 방법 1 (30분, 시간초과)
# def matrix_multi(arr1, arr2):
#     # matrix multiplication
#     num = len(arr1)
#     res = [[0]*num for _ in range(num)]
#     for r in range(num):
#         for c in range(num):
#             for i in range(num):
#                 res[r][c] += arr1[r][i] * arr2[i][c]
#     return res

# def solve(arr, multi):
#     if multi == 1:
#         return arr
#     elif multi % 2 == 0:
#         return matrix_multi(solve(arr, multi//2), solve(arr, multi//2))
#     else:
#         return matrix_multi(solve(arr, multi-1), solve(arr, 1))

# N, B = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(N)]
# res_arr = solve(A,B)
# for i in range(N):
#     for j in range(N):
#         print(res_arr[i][j]%1000, end=' ')
#     print()

# 방법 2 (통과)
def mul(arr1, arr2):
    # matrix multiplication
    num = len(arr1)
    res = [[0]*num for _ in range(num)]
    for r in range(num):
        for c in range(num):
            for i in range(num):
                res[r][c] += arr1[r][i] * arr2[i][c]
            res[r][c] %= 1000
    return res

def solve(arr, multi):
    if multi == 1:
        for r in range(len(arr)):
            for c in range(len(arr)):
                arr[r][c] %= 1000
        return arr
    
    tmp = solve(arr, multi//2)
    if multi % 2 == 0:
        return mul(tmp, tmp)
    else:
        return mul(mul(tmp, tmp), arr)

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
result = solve(A,B)
for r in result:
    print(*r)
