def isPrimeNumber(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    end = int(num ** (1 / 2))
    for i in range(2, end + 1):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    # k진수로 변환
    num_k = ''
    while n > 0:
        num_k = str(n % k) + num_k
        n //= k

    # 조건에 맞는 숫자 고르기
    arr = num_k.split('0')
    print(arr)

    # 조건에 맞는 숫자 중 소수인 수 구하기
    for a in arr:
        # 소수인지 검사
        if a == '':
            continue
        if isPrimeNumber(int(a)):
            answer += 1

    return answer