import copy

N, depth = map(int, input().split())
check = [False for _ in range(N)]
num = [i for i in range(1, N + 1)]
result = []
real_result = []
def suyeol(N, depth):
    if not depth:
        a = copy.deepcopy(result)       # 처음에 result를 바로 real_result에 넣었다가 나중에 값이 다 바뀌어서 deepcopy
        return real_result.append(a)
    for i in range(N):
        if not check[i]:                # 중복되지 않게 체크
            check[i] = True             # 사용 체크
            result.append(num[i])
            depth -= 1
            suyeol(N, depth)
            result.pop()                # 뽑고
            depth += 1                  # 깊이 더하고
            check[i] = False            # 사용 체크 풀고
    return real_result

b = suyeol(N,depth)
for i in range(len(b)):
    print(*b[i])
