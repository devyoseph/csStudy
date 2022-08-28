"""
PGS
합승 택시 요금
level3
40분
https://programmers.co.kr/learn/courses/30/lessons/72413
"""
"""
[플로이드 와샬 알고리즘]
모든 정점에서 모든 정점으로의 최단 경로 구하기
* X에서 Y로 가는 비용 vs X 에서 1로 가는 비용 + 1에서 Y로 가는 비용

다익스트라는 가장 적은 비용을 하나씩 선택했다면, 플로이드 와샬 알고리즘은 거쳐가는 정점을 기준으로 알고리즘을 수행
"""
def solution(n, s, a, b, fares):
    # 결과 그래프 최댓값으로 초기화
    d = [[float("inf")]*(n+1) for _ in range(n+1)]
    # 출발지와 도착지 같은 경우 0으로 초기화
    for i in range(1,n+1):
        d[i][i] = 0
    # 주어진 배열을 결과 그래프에 저장
    for v1,v2,cost in fares:
        d[v1][v2] = cost
        d[v2][v1] = cost

    # 플로이드 와샬로 모든 정점에서 모든 정점으로의 최단경로 구하기
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                # i-j 보다 i-k + k-j 가 더 짧으면(최소비용) 업데이트
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]

    # 모든 정점을 하차 지점으로 생각하여 최소비용 구하기
    answer = min(d[s][i] + d[i][a] + d[i][b] for i in range(1, n+1))
    return answer

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))