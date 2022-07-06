'''
PGS
자물쇠와 열쇠
lv 3
2시간
https://programmers.co.kr/learn/courses/30/lessons/60059
'''
import copy
import numpy
from pprint import pprint


def solution(key, lock):
    answer = False
    n = len(lock)
    if sum(map(sum, lock)) == n*n:
        return True
    def check_zero(modilock):
        n = len(modilock)//3
        for r in range(n):
            for c in range(n):
                if modilock[r+n][c+n]==0:
                    return False
        return True
    def makelock(newmodilock,r,c, n):
        k = len(key)
        for i in range(n):
            for j in range(n):
                if i>=k or j>=k:
                    continue
                elif newmodilock[r + i][c + j] == 0 and key[i][j] == 1:
                    newmodilock[r + i][c + j] = key[i][j]
                elif newmodilock[r + i][c + j] == 1 and key[i][j] == 1:
                    return True

    def check(key, lock):
        # 비교위해 lock 늘리기
        n = len(lock)
        k = len(key)
        modilock = [[0 for _ in range(3*n)] for _ in range(3*n)]
        for r in range(n):
            for c in range(n):
                modilock[r+n][c+n] = lock[r][c]

        for r in range(n-k+1, 2*n-1+1):
            for c in range(n-k+1, 2*n):
                newmodilock = copy.deepcopy(modilock)
                if makelock(newmodilock, r,c, n):
                    continue

                # pprint(newmodilock)
                if check_zero(newmodilock):
                    return True

        return False
    #회전시키기 추가하기
    for i in range(4):
        key = numpy.rot90(key, 1)
        if check(key, lock):
            return True
    return answer


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1,1], [1, 1, 0,1], [1, 0, 1,1],[1,0,1,1]]))