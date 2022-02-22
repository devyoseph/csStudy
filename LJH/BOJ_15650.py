import copy

N, depth = map(int, input().split())
check = [False for _ in range(N)]
num = [i for i in range(1, N + 1)]
result = [0]
real_result = []
def suyeol(N, depth):
    if not depth:
        a = copy.deepcopy(result[1:])       # 앞에 0 자르고 저장
        return real_result.append(a)
    for i in range(N):
        if not check[i] and num[i] > result[-1]:    # 작은 값이 안 오게
            check[i] = True
            result.append(num[i])
            depth -= 1
            suyeol(N, depth)
            result.pop()
            depth += 1
            check[i] = False
    return real_result

b = suyeol(N,depth)
for i in range(len(b)):
    print(*b[i])
