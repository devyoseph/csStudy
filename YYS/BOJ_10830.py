def multi(lst1, lst2):
    global N
    lst = [[0]*N for m in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                lst[i][j] += lst1[i][k]*lst2[k][j]
    for i in range(N):
        for j in range(N):
            lst[i][j] %= 1000
    return lst

def dfs(B):
    global lst,N
    
    if B == 1:
        return lst

    tmp = dfs(B//2)

    if B % 2 ==0:
        return multi(tmp,tmp)
    else:
        return multi(multi(tmp,tmp),lst)



N, B = list(map(int,input().split()))
lst = []
for i in range(N):
    lst.append(list(map(int,input().split())))

ans = dfs(B)
for i in range(N):
    for j in range(N):
        ans[i][j] %= 1000
for i in ans:
    print(*i)