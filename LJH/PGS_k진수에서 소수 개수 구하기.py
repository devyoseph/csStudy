# def solution(n, k):
#     newn = 0
#     while n!=0:
#         newn = newn*10 + n//k
#         n %= k
#     answer = -1
#     return answer

n, k = map(int, input().split())
newn = ''
while n!=0:
    newn = str(n%k) + newn
    n //= k
newn += '0'
# print(newn)
cnt = 0
# 소수 체크
def sosu(n):
    global cnt
    if not n:
        return
    temp = int(n)
    if temp==1:
        return
    for i in range(2,int(temp**0.5)):
        if temp%i==0:
            return
    cnt += 1
    return


if '0' not in newn:
    sosu(newn)

flag = False
check = 0
for i in range(len(newn)):
    if newn[i]=='0':
        flag = not flag
    if flag:
        sosu(newn[check:i])
        check = i+1
        flag = not flag

print(cnt)