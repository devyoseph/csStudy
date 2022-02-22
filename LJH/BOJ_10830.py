
# def square(lst, lst2, B):       # 원형 행렬, 제곱된 행렬, 제곱 횟수
#     if B == 1:
#         for i in range(N):
#             for j in range(N):
#                 lst2[i][j] %= 1000
#         return lst2
#     new_lst = [[0] * N for _ in range(N)]
#     for r in range(len(lst)):
#         for c in range(len(lst)):
#             for k in range(len(lst)):
#                 new_lst[r][c] += lst[r][k]*lst2[k][c]
#     return square(lst, new_lst, B-1)
######
# if B >= 2 and len(lst) <= int(log2(B)) + 1:
#     if B % 2:
#         lst.append(power(A, B // 2) ** 2 * A)
#     else:
#         lst.append(power(A, B // 2) ** 2)
# return lst[int(log2(B))+1]

def mult(lst1, lst2):
    new_lst = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            for k in range(N):
                new_lst[r][c] += lst1[r][k]*lst2[k][c]
            new_lst[r][c] %= 1000
    return new_lst



def square(lst, B):
    # global cnt
    # cnt += 1
    if B == 1:
        return A
    temp = square(lst, B // 2)
    if B%2:
        return  mult((mult(temp, temp)), A)
    else:
        return mult(temp, temp)



# cnt = 0
N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
main_list = [A, A]
result = square(A, B)
for i in range(N):
    for j in range(N):
        result[i][j] %= 1000
# print(cnt)
for i in result:
    print(*i)
