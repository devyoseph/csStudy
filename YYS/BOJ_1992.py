def dfs(row, col, N): # L은 글자
    global lst

    S = lst[row][col] # 글자 추출
    judge = True
    L = ''
    # 모두 같은 색인지 검사하는 부분
    for i in range(N):
        for j in range(N):
            if S != lst[row+i][col+j]:
                judge = False
                break
    if judge:
        L = S
    else:
        L = '('+dfs(row, col, N // 2)+dfs(row, col + N // 2, N // 2)+dfs(row + N // 2, col, N // 2)+dfs(row + N // 2, col + N//2, N // 2)+')'

    return L

N = int(input())
lst = []

for i in range(N):
    lst.append(input()) # 문자열이 들어갑니다

print(dfs(0, 0, N))