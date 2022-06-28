
import sys
input = sys.stdin.readline

def isPell(S, E):
    global dp, arr
    
    if S >= E: # 가운데 두 개 문자가 남았을 때 서로 감소하면서 엇갈리는 문제 발생 (=에서 >=로 수정)
        return 1
    elif dp[S][E] == -1:

        # 외곽 숫자가 같으면 그 내부 dp가 존재하는지 확인하고 맞으면 펠린드롬으로 정의
        if arr[S] == arr[E] and isPell(S+1, E-1) == 1:
            dp[S][E] = 1
        else:
            dp[S][E] = 0

    return dp[S][E]


N = int(input())
dp = [[-1 for _ in range(N+1)] for __ in range(N+1)]
arr = list(map(int, input().split()))
arr.insert(0,0) # 번호 맞추기 위해 맨 앞에 숫자 추가

M = int(input())

for m in range(M):
    S, E = map(int, input().split())
    print(isPell(S,E))