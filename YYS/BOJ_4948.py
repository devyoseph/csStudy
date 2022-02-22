import math

while True:
    N = int(input()) # N을 입력 받고
    if not N: break; # 0이면 반복문을 바로 종료합니다

    lst = [True for i in range(2*N+1)] # 2N+1 크기의 리스트를 만들고
    lst[1] = False # 1은 지워줍니다
    
    for i in range(2, int(math.sqrt(2*N+1))+2): # 2부터 루트 2N+1까지 지워줍니다
        if lst[i]:
            start = 2 # 현재수의 2배부터 지워줍니다
            while i*start <= 2*N:
                lst[i*start] = False
                start += 1
    
    # 정답 출력부            
    sum = 0
    for i in range(N+1, 2*N+1): # 범위 주의 (N보다 크고 2N 보다 같거나 작은 수)
        if lst[i]:
            sum += 1
            
    print(sum)