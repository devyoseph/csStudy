import sys
read = sys.stdin.readline



# def w(a, b, c):               # 리스트
#     if a <= 0 or b <= 0 or c <= 0:
#         return 1
#     elif a > 20 or b > 20 or c > 20:
#         return w(20,20,20)
#     elif not lst[a][b][c]:
#         if a < b < c:
#             lst[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
#             return lst[a][b][c]
#         else:
#             lst[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
#             return lst[a][b][c]
#     else:
#         return lst[a][b][c]
#
# lst = [[[0]*21 for _ in range(21)] for _ in range(21)]


def w(a, b, c):             # 딕셔너리
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20,20,20)

    key = f'{a} {b} {c}'

    if key in cache:
        return cache[key]
    res = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    cache[key] = res

    return res

cache = {}


while True:
    a, b, c = map(int, read().split())          # input -> 1012ms, read() -> 112ms
    if a == -1 and b == -1 and c == -1:         # list냐 dict냐는 차이 별로 안 남
        break
    res = w(a, b, c)
    print(f'w({a}, {b}, {c}) = {res}')