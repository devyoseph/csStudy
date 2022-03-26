
def check(row):
    global cnt
    bridge = [0]*len(row)
    for i in range(len(row)-1):
        d = row[i] - row[i + 1]
        if d==0:
            continue
        elif d==1:
            for k in range(L):
                if 0<=i+k+1<N and bridge[i+k+1]==0 and row[i+k+1]==row[i]-1: # 경사로를 놓다가 범위를 벗어나는 경우, 경사로를 놓은 곳에 또 경사로를 놓는 경우, 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
                    bridge[i+k+1]=1
                else:
                    return
        elif d==-1:
            for k in range(L):
                if 0<=i-k<N and bridge[i-k]==0  and row[i-k]==row[i]:   # 이 경우는 자기 자신부터 경사로 놓기 시작함
                    bridge[i-k]=1
                else:
                    return
        else:
            return  # 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
    cnt += 1

N, L = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
for row in lst:
    check(row)
for row in list(zip(*lst)):
    check(row)
print(cnt)
