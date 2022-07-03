# 반례들을 참고...
# 회전은 그렇다치고 굳이 이동이 필요할까? 격자의 관계를 파악한다. => 판끼리 만나면 안된다는 조건 때문에 반례 발생 => key를 돌려서 집어넣는다
# 문제가 짧을수록 조건을 자세히 읽어야 한자
import copy

def solution(key, lock):
    global GRID, M, judge

    def check(r, c, lock, KEY_ARR, k):  # KEY 내에서 확인, k번쨰 index 기준으로 관계도 작성
        temp_KEY_ARR = [] # 새로운 관계도 작성
        temp_row = KEY_ARR[k][0] # k번째 원소가 기준이 됨
        temp_col = KEY_ARR[k][1]
        
        for keyarr in KEY_ARR:
            temp_KEY_ARR.append([keyarr[0]-temp_row, keyarr[1]-temp_col]) # 굳이 첫번째가 0,0이 아니어도 돌아감
            
        count = 0
        rest = len(KEY_ARR) + 1  # 나머지
        for k in range(len(KEY_ARR)):
            rest -= 1  # 진행될 때마다 감소

            if count + rest < GRID: # 뒤에 모든 키를 맞춰도 격자 개수를 따라잡지 못하면 False
                return False

            row = r + temp_KEY_ARR[k][0]
            col = c + temp_KEY_ARR[k][1]

            if row < 0 or row >= N or col < 0 or col >= N:
                continue

            if lock[row][col] == 1:
                return False # 판끼리 만나면 불가능

            elif lock[row][col] == 0: # key는 1이므로 0이랑 만나야 count
                count += 1

        return True if count == GRID else False

    M = len(key)
    N = len(lock)
    GRID = 0

    # key 정보 뽑아내기: 쐐기의 개수(GRID), 관계도: GRID_ARR
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                GRID += 1
    
    # 이미 맞춰져있으면 굳이 풀 필요가 없다
    if GRID == 0:
        return True
    
    # 회전한 값을 임시 저장
    rotate_key = [[0 for _ in range(M)] for __ in range(M)]

    judge = False  # 만약 하나라도 true면 열 수 있음
    for k in range(4):  # 회전은 4번
        for i in range(M):
            for j in range(M):
                rotate_key[i][j] = key[M - 1 - j][i]

        key = copy.deepcopy(rotate_key)
        KEY_ARR = []
        for i in range(M):
            for j in range(M):
                if key[i][j] == 1:
                    KEY_ARR.append([i, j])

        for i in range(N):
            for j in range(N):
                for k in range(len(KEY_ARR)):
                    if lock[i][j] == 0 and check(i, j, lock, KEY_ARR, k):
                        return True
    return False



print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]))