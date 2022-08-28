"""
BOJ
행렬 곱셈
브론즈1
20분
https://www.acmicpc.net/problem/2740
"""
def mat_mul (arr1, arr2):
    res = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for r in range(len(arr1)):
        for c in range(len(arr2[0])):
            for i in range(len(arr1[0])):
                res[r][c] += arr1[r][i] * arr2[i][c]
    return res

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

arr = mat_mul(A, B)
for a in arr:
    print(*a)