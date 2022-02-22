num = int(input())
sign = input().split()

answer = [0 for i in range(num+1)] # 정답을 기록할 배열
check = [False for i in range(10)] # 방문 체크용
findMax = False # 값을 찾으면 메소드를 바로 종료하기 위해 존재

def locate(num, depth): # 그 위치에 넣을 수 있는지 판단해주는 메소드
    if depth == 0:
        return True
    else:
        if sign[depth-1] == '>':
            return True if answer[depth-1] > num else False
        else:
            return True if answer[depth - 1] < num else False

def backtrack(depth): # 백트래킹 구현
    if depth == num+1: # 깊이가 목표에 도달하면 값을 출력하고 모든 재귀 종료
        print(''.join(map(str,answer))) # 모아둔 리스트 값 출력
        global findMax
        findMax = True
        return

    for i in range(9,-1,-1): # 9부터 내려오면서 검사 = 최대값
        if not check[i] and locate(i,depth):
            check[i] = True # 방문 표시
            answer[depth] = i # 값 저장
            backtrack(depth+1)
            if findMax:
                return
            check[i] = False # 재귀를 빠져나오면 방문 해제

def backtrack2(depth):
    if depth == num+1:
        print(''.join(map(str,answer)))
        global findMax
        findMax = True
        return

    for i in range(0,10,1): # 0부터 출발해 최소값을 얻어냄
        if not check[i] and locate(i,depth):
            check[i] = True # 방문
            answer[depth] = i
            backtrack2(depth+1)
            if findMax:
                return
            check[i] = False

backtrack(0)
answer = [0 for i in range(num+1)] # 기존 변수들 초기화
check = [False for i in range(10)]
findMax = False
backtrack2(0)