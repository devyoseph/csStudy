import sys
sys.stdin = open("sample_input (1).txt", "r")

T = int(input())

def sol(n,lst):
    global res, N
    if n>=res:
        return
    if n==6:
        res = min(res, float('inf'))
        return
    for i in range(1,N):
        newlist = lst[:]
        if 0<=i<N//2:
            left = newlist[:N//2] + [0 for _ in range(N//2)]
            right = newlist[N//2:]
        else:
            left = newlist[N // 2:] + [0 for _ in range(N // 2)]
            right = newlist[:N // 2]
            i = N-i-1
        j=0
        [1,2,3,4,5,6]
        [1,2,3,0,0,0]
        [4,5,6]
        while i!=j:
            kk = 0
            for k in range(i-j):
                if (N//2-1+kk+1)==N:
                    break
                else:
                    # 반에서 왼쪽꺼랑 +1한거 버블 소트 느낌으로 교환하고
                    # 다음 for문은 반에서 왼쪽꺼 -1한거를 버블 소트
                    left[N//2-1-j+kk], left[N//2-1-j+kk+1] = left[N//2-1-j+kk+1], left[N//2-1-j+kk]
                    kk+=1
            j+=1
        j=0
        [1,0,2,0,3,0]
        for i in range(N):
            # 빈 자리 채우기
            if left[i]==0:
                left[i] = right[j]
                j+=1
        if left == reslist or left == revlist:
            res = min(res, n)
            break
        sol(n+1, left)




for tc in range(1, T+1):
    N = int(input())
    res = float('inf')
    lst = list(map(int, input().split()))
    reslist = sorted(lst)
    revlist = sorted(lst,reverse=True)
    if lst == reslist or lst == revlist:
        print(f'#{tc} 0')
        continue
    sol(1,lst)
    if res==float('inf'):
        res = -1
    print(f'#{tc} {res}')