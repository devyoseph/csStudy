# 카운팅 정렬
lst = [False for i in range(2000001)]
n = int(input())
for i in range(n):
    lst[int(input())+1000000] = True
for i in range(2000001):
    if lst[i]:
        print(i-1000000)