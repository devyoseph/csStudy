N = int(input())

# def fibo(N):
#     if N == 1 or N == 0:
#         return memo[1]
#     else:
#         if len(memo)<=N:
#             memo.append((fibo(N - 1) + fibo(N - 2))%15746)
#     return memo[N]

def fibo1(N):
    start = 1
    while start!=N+1:
        start += 1
        memo.append((memo[start-1]+memo[start-2])%15746)
    return memo[N]

memo = [1, 1]
a = fibo1(N)
print(a%15746)