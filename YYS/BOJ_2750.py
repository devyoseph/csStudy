n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
for i in range(n):
    for j in range(n-i-1):
        if lst[j] > lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
for i in lst:
    print(i)