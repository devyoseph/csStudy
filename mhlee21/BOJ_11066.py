"""
BOJ
파일 합치기
골드3
-
https://www.acmicpc.net/problem/11066
"""
# 참고 https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-11066-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%8C%8C%EC%9D%BC-%ED%95%A9%EC%B9%98%EA%B8%B0-%EA%B3%A8%EB%93%9C3-DP

import sys

T = int(input())
for test_case in range(T):
    K = int(input())
    arr = list(map(int, input().split()))

    # 연속합, 여러번 sum 함수를 사용하지 않아도 되어 효율적
    subSum = [0]
    for i in arr:
        subSum.append(subSum[-1] + i)

    # dp를 2차원 리스트로 만든다.
    ## 시작점과 끝점을 정해준다고 생각
    dp = [[0]*(K+1) for _ in range(K+1)]


    # 최종 점화식 : dp[i][j] = dp[i][k] + dp[k+1][j] + sum[j+1] - sum[i]
    for size in range(1,K):
        for start in range(K-size):
            end = start+size
            dp[start][end] = sys.maxsize
            # 전체 그룹을 두 그룹으로 나눈 뒤, 각 그룹을 최소 비용이 되게 압축하면,
            # 압축된 두 수를 더한 값과 두 그룹의 최소 비용의 합이
            # 분할 이전 전체 그룹의 최소 비용이다.
            for cut in range(start,end):
                dp[start][end] = min(dp[start][end], dp[start][cut] + dp[cut+1][end] + subSum[end+1] - subSum[start])

    print(dp[0][K-1])