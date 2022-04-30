import sys
sys.stdin = open('input.txt', 'r')

INF = float("inf")

T = int(input())
for test_case in range(1,T+1):
    N, M, X = map(int, input().split())  # 집의 수, 도로의 수, 인수의 집
    '''
    X번 집으로 오고 가는데 드는 시간 중에서 가장 오래 걸리는 집은 얼마나 걸리는지 구하기
    '''
    d = [[INF]*N for _ in range(N)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        d[x-1][y-1] = c

    for k in range(N):          # 거쳐가는 노드
        for i in range(N):      # 출발 노드
            for j in range(N):  # 도착 노드
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    res = 0
    for idx in range(N):
        res = max(res,d[idx][X-1]+d[X-1][idx])

    print(f'#{test_case} {res}')