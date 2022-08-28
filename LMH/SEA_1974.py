"""
SEA
스도쿠 검증
D2
30분
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq
"""

def check(lst):
    sorted_list = sorted(lst)
    for i in range(9):
        if sorted_list[i] != (i+1):
            return False
    return True

T = int(input())
for test_case in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    trans_arr = list(map(list, zip(*arr)))
    arr_3x3 = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            arr_3x3.append(arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3])

    res = 1
    for i in range(9):
        if not check(arr[i]) or not check(trans_arr[i]) or not check(arr_3x3[i]):
            res = 0

    print(f'#{test_case} {res}')