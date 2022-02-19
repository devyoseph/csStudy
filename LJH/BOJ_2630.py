

dict = {
    '1': 0,
    '0': 0,
}

def checksame(lst):
    global dict
    if len(lst) == 1:       # 마지막까지 쪼개졌을 때
        dict[str(lst[0][0])] += 1
        return False
    a = 0
    b = lst[0][0]
    for i in range(len(lst)):
        for j in range(len(lst)):
            a += lst[i][j]
            b *= lst[i][j]
    if a>0 and b == 1:      # 다 1일 떄
        dict['1'] += 1
        return False
    elif a == 0 and b == 0:
        dict['0'] += 1
        return False
    else:
        return True


def check(lst):
    global dict
    N = len(lst)
    if checksame(lst):
        lst1 = [[0]*(len(lst)//2) for _ in range(len(lst)//2)]
        lst2 = [[0]*(len(lst)//2) for _ in range(len(lst)//2)]
        lst3 = [[0]*(len(lst)//2) for _ in range(len(lst)//2)]
        lst4 = [[0]*(len(lst)//2) for _ in range(len(lst)//2)]
        for i in range(N):                          # 이 부분을 함수 입력 받을 때 시작하는 i,j로 입력을 받으면 좋을듯
            for j in range(N):
                if i<N//2 and j<N//2:
                    lst1[i][j] = lst[i][j]
                elif i<N//2 and j>=N//2:
                    lst2[i][j-N//2] = lst[i][j]
                elif i>=N//2 and j<N//2:
                    lst3[i-N//2][j] = lst[i][j]
                elif i>=N//2 and j>=N//2:
                    lst4[i-N//2][j-N//2] = lst[i][j]
        if checksame(lst1):
            check(lst1)
        if checksame(lst2):
            check(lst2)
        if checksame(lst3):
            check(lst3)
        if checksame(lst4):
            check(lst4)
    else:
        return

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
check(lst)
print(dict['0'])
print(dict['1'])