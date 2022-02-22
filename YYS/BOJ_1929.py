M, N = list(map(int,input().split()))
prime = [True for i in range(N+1)] # N+1 크기의 배열형 리스트 완성
prime[1] = False # 1은 소수x

def checkPrime(num):
    n = num*2
    while n <= N:
        prime[n] = False
        n += num

for i in range(2,N//2+1):
    if prime[i]:
        checkPrime(i)

for i in range(M,N+1):
    if prime[i]:
        print(i)