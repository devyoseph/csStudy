import math
def primeTest(N):
    if N == 1: return False
    for i in range(2, int(math.sqrt(N)+1)):
        if N % i == 0: return False
    return True

def solution(n, k):
    # 에라토스테네스의 체 ++?
    # 최대 소수의 크기?
    # 999,999(10) 겁나큼 
    string = ''
    cnt = 0
    while n != 0:
        mod = n % k
        string = str(mod) + string
        n //= k
    for i in string.split('0'):
        if i != '' and primeTest(int(i)):
            cnt += 1

    return cnt
print(solution(437674, 3))