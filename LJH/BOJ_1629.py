from math import log2

# cnt = 0
# def power(A,B):
#     global cnt
#     cnt += 1
#     if B == 1:
#         return A
#     if B>=2 and len(lst) <= int(log2(B))+1:
#         temp = power(A, B//2)
#         if B%2:
#             lst.append(temp *temp * A)
#         else:
#             lst.append(temp *temp)
#     return lst[int(log2(B))+1]

def power(A,B):
    if B == 1:
        return A
    temp = power(A, B//2)                   # 하나로 저장해서 여러번 호출을 막는 듯?
    if B%2:
        return temp * temp * A %C           # 매 결과에 C를 나눠주면 시간이 많이 주는 듯?
    else:
        return temp * temp%C


A, B, C = map(int, input().split())
print(power(A,B)%C)

