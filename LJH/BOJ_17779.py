

def sol():
    lst5 = [[0]*N for _ in range(N)]
    ccl = 0
    cclb = True
    ccr = 0
    ccrb = True
    for rr in range(r,r+d1+d2+1):
        for cc in range(c-d1,c+d2+1):
            if c - ccl<=cc<=c+ccr:
                lst5[rr][cc]=1
        if cclb and ccl >= d1:
            cclb = False
        if ccrb and ccr >= d2:
            ccrb = False
        if cclb:
            ccl += 1
        else:
            ccl -= 1
        if ccrb:
            ccr += 1
        else:
            ccr -= 1
    # print(lst5)


    # if d1>d2:
    #     while rr<=d2:
    #         for cc in range(c-rr,c+rr+1):
    #             lst5.append([r+rr,cc])
    #         rr += 1
    #     while d2<rr<=d1:
    #         for cc in range(c-rr,c+2*d2-rr+1):
    #             lst5.append([r+rr,cc])
    #         rr += 1
    #     while d1<rr<=d1+d2:
    #         for cc in range(c-2*d1+rr,c+2*d2-rr+1):
    #             lst5.append([r+rr,cc])
    #         rr += 1
    # elif d1<d2:
    #     while rr<=d1:
    #         for cc in range(c-rr,c+rr+1):
    #             lst5.append([r+rr,cc])
    #         rr += 1
    #     while d1<rr<=d2:
    #         for cc in range(c-2*d1+rr,c+rr+1):
    #             lst5.append([r+rr,cc])
    #         rr += 1
    #     while d2<rr<=d1+d2:
    #         for cc in range(c-2*d1+rr,c+2*d2-rr+1):
    #             lst5.append([r+rr,cc])
    #         rr += 1
    # elif d1==d2:
    #     while rr<=d2:
    #         for cc in range(c-rr,c+rr+1):
    #             lst5.append([r+rr,cc])
    #         rr += 1
    #     # while d2<=rr<d1:
    #     #     for cc in range(c-rr,c+2*d2-rr):
    #     #         lst5.append([r+rr,cc])
    #     #     rr += 1
    #     while d1<rr<=d1+d2:
    #         for cc in range(c-2*d1+rr,c+2*d2-rr+1):
    #             lst5.append([r+rr,cc])
    #         rr += 1


    lst12345 = [0] * 5
    for i in range(N):
        for j in range(N):
            if lst5[i][j]==0:
                if 0 <= i < r + d1 and 0 <= j < c + 1:
                    lst12345[0] += lst[i][j]
                elif 0 <= i <= r + d2 and c + 1 <= j < N:
                    lst12345[1] += lst[i][j]
                elif r + d1 <= i < N and 0 <= j < c - d1 + d2:
                    lst12345[2] += lst[i][j]
                elif r + d2 < i < N and c - d1 + d2 <= j < N:
                    lst12345[3] += lst[i][j]
            else:
                lst12345[4] += lst[i][j]
    return max(lst12345) - min(lst12345)

    # return lst5

# def sol2():
#     lst12345 = [0]*5
#     for i in range(N):
#         for j in range(N):
#             if [i, j] not in lst5:
#                 if 0<=i<r+d1 and 0<=j<c+1:
#                     lst12345[0] += lst[i][j]
#                 elif 0<=i<=r+d2 and c+1<=j<N:
#                     lst12345[1] += lst[i][j]
#                 elif r+d1<=i<N and 0<=j<c-d1+d2:
#                     lst12345[2] += lst[i][j]
#                 elif r+d2<i<N and c-d1+d2<=j<N:
#                     lst12345[3] += lst[i][j]
#             else:
#                 lst12345[4] += lst[i][j]
#     return max(lst12345)-min(lst12345)

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
res = 10**10
for r in range(N-2):
    for c in range(1,N-1):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if c-d1>=0 and c+d2<N and r+d1+d2<N:
                    # lst5 = sol()
                    # temp = sol2()
                    temp = sol()
                    res = min(res,temp)
print(res)

