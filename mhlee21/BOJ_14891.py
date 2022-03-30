"""
BOJ
톱니바퀴
골드5
1시간
https://www.acmicpc.net/problem/14891
"""
def spin(n,d,gear):
    # 왼쪽 톱니바퀴
    if n <= gear and n > 0 and arr[n][6] != arr[n-1][2]:
        spin(n-1, -d, gear)
    # 오른쪽 톱니바퀴
    if n >= gear and n < 3 and arr[n][2] != arr[n+1][6]:
        spin(n+1, -d, gear)
    # 현재 톱니바퀴
    tmp = arr[n]
    if d == 1: # 시계방향
        end = tmp.pop()
        tmp = [end] + tmp
    elif d == -1: # 반시계방향
        start = tmp.pop(0)
        tmp = tmp + [start]
    arr[n] = tmp

def get_score():
    res = 0
    for i in range(4):
        if arr[i][0]:
            res += (1<<i)
    return res

arr = [list(map(int,input())) for _ in range(4)]
K = int(input())
for _ in range(K):
    num, dist = map(int, input().split())
    spin(num-1,dist,num-1)
print(get_score())